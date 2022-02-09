import copy
import imp
import traceback
import class_forprocess
import specific_class
import time

# 大域変数の先頭にはG_をつける(Global)


class MakeCssClass:
    def __init__(self):
        self.G_NG_TAGS = ["div", "body"]
        self.G_NG_TAGS_Message = "不適切なブロック名が設定されました 使用禁止:" + " ".join(self.G_NG_TAGS)
        # animationプロパティを使う

        self.G_specific_class_types = specific_class.class_name_list

        self.G_parent = ""
        self.G_block_queue = []
        self.G_keyframe_queue = []

        self.G_DEBUG_MODE = True

        self.G_outputfileName = 'sample.css'

        self.G_outputfile = open(self.G_outputfileName, "w")
    # ここが呼ばれる

    def processMain(self, root_class, write_path):

        self.write_reception_parent_start()

        self.write_reception_parent_enter(root_class.scope + "{\n")

        # self.G_parent + root_class.scope
        for roop_shape in root_class.Shapes:
            self.block(root_class, roop_shape)

        self.write_reception_parent_enter("}")

        self.write_reception_parent_end()

        self.EndProcess()

    # 終了処理

    def EndProcess(self):
        self.G_outputfile.close()

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    def comment_process(self, text):
        return "/* " + text + " */\n"

    def indent_process(self, text, indent):
        for i in range(indent):
            text = "   " + text
            print("indent_process", indent, text)
        return text

    def write_reception_parent_start(self):
        pass

    def write_reception_keyframe_start(self):
        self.G_keyframe_queue.append("")

    def write_reception_block_start(self):
        self.G_block_queue.append("")

    def write_reception_parent_enter(self, text, comment=False, indent=0):
        text = self.indent_process(text, indent)
        if comment:
            text = self.comment_process(text)
        self.G_parent += text

        print(self.G_parent)

    def write_reception_block_enter(self, text, comment=False, indent=0):
        text = self.indent_process(text, indent)
        if comment:
            text = self.comment_process(text)
        self.G_block_queue[-1] += text

        print(self.G_block_queue)

    def write_reception_keyframe_enter(self, text, comment=False, indent=0):
        text = self.indent_process(text, indent)
        if comment:
            text = self.comment_process(text)
        self.G_keyframe_queue[-1] += text

        print(self.G_keyframe_queue)

    def write_reception_parent_end(self):
        self.G_outputfile.write(self.G_parent)

    def write_reception_block_end(self):
        self.G_outputfile.write(self.G_block_queue[-1])

    def write_reception_keyframe_end(self):
        self.G_outputfile.write(self.G_keyframe_queue[-1])

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    def block(self, root_class, shape_data):
        self.write_reception_block_start()
        self.write_reception_block_enter("blockの生成順序{0}".format(len(self.G_block_queue)), comment=True)

        for roop_animation in shape_data.animations:
            self.animation_block(roop_animation)

        if len(root_class.scope) > 0:  # CSSセレクタの設定
            self.write_reception_block_enter("{0}>".format(root_class.scope))

        if shape_data.block_name in self.G_NG_TAGS:
            raise Exception(self.G_NG_TAGS_Message)

        self.write_reception_block_enter("{0}".format("."+shape_data.block_name)+"{\n")
        self.write_reception_block_enter("position:absolute;\n", indent=1)
        self.block_index_by_animation_options(shape_data.animations)
        self.block_index(shape_data)
        self.write_reception_block_enter("}\n")

        self.write_reception_block_end()

    def block_index(self, shape_data):
        for k, v in zip(shape_data.shape_index_dict.keys(), shape_data.shape_index_dict.values()):
            return_val = self.specific_class_inspection(v[0])

            if return_val is None:
                self.write_reception_block_enter("{0} : {1}{2};\n".format(k, v[0], v[1]), indent=1)

            else:
                self.write_reception_block_enter("{0} : {1};\n".format(k, return_val), indent=1)

            print("kv", k, v, return_val)

    def block_index_by_animation_options(self, shape_data_animations):

        if len(shape_data_animations) == 0:
            return

        self.write_reception_block_enter("animation:", indent=1)

        for roop, roop_animation in enumerate(shape_data_animations):
            options_values = roop_animation.animation_options.values()

            for ov in options_values:
                # print(type(ov))
                if type(ov) is list:
                    self.write_reception_block_enter(" {0}{1}".format(ov[0], ov[1]))
                else:
                    self.write_reception_block_enter(" {0}".format(ov))

            if roop < len(shape_data_animations) - 1:
                print(roop, len(shape_data_animations)-1)
                self.write_reception_block_enter(",")

        self.write_reception_block_enter(";\n")

    def animation_block(self, animation):

        # animation.animation_index_dict
        self.write_reception_keyframe_start()
        self.write_reception_keyframe_enter("animationの生成順序{0}".format(len(self.G_keyframe_queue)), comment=True)

        self.write_reception_keyframe_enter("@keyframes {0}".format(animation.animation_options["name"])+"{\n")
        for ail in animation.animation_index_list:

            return_val = self.specific_class_inspection(ail[2])

            self.write_reception_keyframe_enter("{0}{1}\n".format(ail[0], "% {"), indent=1)
            if return_val is None:
                self.write_reception_keyframe_enter("{0}:{1}{2};\n".format(ail[1], ail[2], ail[3]), indent=2)
            else:
                self.write_reception_keyframe_enter("{0}:{1};\n".format(ail[1], return_val), indent=2)
            self.write_reception_keyframe_enter("}\n", indent=1)

        self.write_reception_keyframe_enter("}\n")
        self.write_reception_keyframe_end()

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # 特定のclassだった時にget_elementを引っ張ってくる

    def specific_class_inspection(self, class_data):
        type_class_data = type(class_data).__name__
        print("tt", type_class_data, self.G_specific_class_types)

        if type_class_data in self.G_specific_class_types:
            print("in", type_class_data)

            return class_data.get_element()

        return None
