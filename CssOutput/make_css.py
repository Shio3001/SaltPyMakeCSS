import copy
import imp
import traceback
from . import class_forprocess
from . import specific_class
import time
import datetime
import inspect
# 大域変数の先頭にはG_をつける(Global)
# 出力に関わる変数および関数の先頭にはWをつける(write)


def G_get_time():
    dt_now = datetime.datetime.now()
    text = dt_now.strftime('%Y/%m/%d/ %H:%M:%S:%f')
    return text


class MakeCssClass:
    def __init__(self):
        self.G_NG_TAGS = ["div", "body"]
        self.G_NG_TAGS_Message = "不適切なブロック名が設定されました 使用禁止:" + " ".join(self.G_NG_TAGS)
        # animationプロパティを使う

        self.G_specific_class_types = specific_class.G_class_name_list

        self.GW_parent = ""
        self.GW_block_queue = []
        self.GW_keyframe_queue = []
        self.GW_log = ""

        self.G_DEBUG_MODE = True

        self.G_outputfileName = 'sample'

        self.G_outputfile = open(self.G_outputfileName+".css", "w")
        self.G_logfile = open(self.G_outputfileName+"_log.txt", "w")

        self.G_addeds_animation = []
    # ここが呼ばれる

    def processMain(self, root_class, write_path):

        self.W_write_reception_parent_start()
        self.W_write_reception_log_start()

        self.W_write_reception_parent_enter(root_class.scope + "{\n")
        self.W_write_reception_parent_enter("position:relative;\n", indent=1)

        # self.GW_parent + root_class.scope
        for roop_shape in root_class.Shapes:
            self.block(root_class, roop_shape)

        self.W_write_reception_parent_enter("}")
        self.W_write_reception_parent_end()
        self.W_write_reception_log_end()

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

    def W_write_reception_parent_start(self):
        pass

    def W_write_reception_keyframe_start(self):
        self.GW_keyframe_queue.append("")

    def W_write_reception_block_start(self):
        self.GW_block_queue.append("")

    def W_write_reception_log_start(self):

        self.W_write_reception_log_enter("ここよりログ")

    def W_write_reception_parent_enter(self, text, comment=False, indent=0):
        text = self.indent_process(text, indent)
        if comment:
            text = self.comment_process(text)

        self.W_write_reception_log_enter("parent/入力要求がありました : {0}".format(text))
        self.GW_parent += text

        print(self.GW_parent)

    def W_write_reception_block_enter(self, text, comment=False, indent=0):
        text = self.indent_process(text, indent)
        if comment:
            text = self.comment_process(text)
        self.W_write_reception_log_enter("block/入力要求がありました : {0}".format(text))
        self.GW_block_queue[-1] += text

        print(self.GW_block_queue)

    def W_write_reception_keyframe_enter(self, text, comment=False, indent=0):
        text = self.indent_process(text, indent)
        if comment:
            text = self.comment_process(text)
        self.W_write_reception_log_enter("keyframe/入力要求がありました : {0}".format(text))
        self.GW_keyframe_queue[-1] += text

        print(self.GW_keyframe_queue)

    def W_write_reception_log_enter(self, text, error=False):

        if error:
            pass

        text = text.replace("/*", "")
        text = text.replace("*/", "")
        text = text.replace("\n", "")

        text = "発生時刻{0}: 関数名:{2}:{3}\n".format(G_get_time(), inspect.stack()[1].filename, inspect.stack()[1].function, text)

        self.GW_log += text

    def W_write_reception_parent_end(self):
        self.W_write_reception_parent_enter("\n")
        self.G_outputfile.write(self.GW_parent)

        self.W_write_reception_log_enter("parentがファイルに書き込まれました")

    def W_write_reception_block_end(self):
        self.W_write_reception_block_enter("\n")
        self.G_outputfile.write(self.GW_block_queue[-1])

        self.W_write_reception_log_enter("blockがファイルに書き込まれました")

    def W_write_reception_keyframe_end(self):
        self.W_write_reception_keyframe_enter("\n")
        self.G_outputfile.write(self.GW_keyframe_queue[-1])

        self.W_write_reception_log_enter("keyframeがファイルに書き込まれました")

    def W_write_reception_log_end(self):
        self.W_write_reception_log_enter("ログを終了します")
        self.G_logfile.write(self.GW_log)

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    def block(self, root_class, shape_data):
        self.W_write_reception_block_start()
        self.W_write_reception_block_enter("blockの生成順序{0}".format(len(self.GW_block_queue)), comment=True)

        for roop_animation in shape_data.animations:
            self.animation_block(roop_animation)

        if len(root_class.scope) > 0:  # CSSセレクタの設定
            self.W_write_reception_block_enter("{0}>".format(root_class.scope))

        if shape_data.block_name in self.G_NG_TAGS:
            raise Exception(self.G_NG_TAGS_Message)

        self.W_write_reception_block_enter("{0}".format("."+shape_data.block_name)+"{\n")
        self.W_write_reception_block_enter("position:absolute;\n", indent=1)
        self.block_index_by_animation_options(shape_data.animations)
        self.block_index(shape_data)
        self.W_write_reception_block_enter("}\n")

        self.W_write_reception_block_end()

        self.W_write_reception_log_enter("{0}が生成されました".format(shape_data.block_name))

    def block_index(self, shape_data):
        for k, v in zip(shape_data.shape_index_dict.keys(), shape_data.shape_index_dict.values()):
            return_val = self.specific_class_inspection(v[0])

            if return_val is None:
                self.W_write_reception_block_enter("{0} : {1}{2};\n".format(k, v[0], v[1]), indent=1)

            else:
                if not v[1] is None:
                    self.W_write_reception_block_enter("{0} : {1};\n".format(k, v[1], return_val), indent=1)
                else:
                    self.W_write_reception_block_enter("{0} : {1};\n".format(k, return_val), indent=1)

            print("kv", k, v, return_val)

    def block_index_by_animation_options(self, shape_data_animations):

        if len(shape_data_animations) == 0:
            return

        self.W_write_reception_block_enter("animation:", indent=1)

        for roop, roop_animation in enumerate(shape_data_animations):
            options_values = roop_animation.animation_options.values()

            for ov in options_values:
                # print(type(ov))
                if type(ov) is list:
                    self.W_write_reception_block_enter(" {0}{1}".format(ov[0], ov[1]))
                else:
                    self.W_write_reception_block_enter(" {0}".format(ov))

            if roop < len(shape_data_animations) - 1:
                print(roop, len(shape_data_animations)-1)
                self.W_write_reception_block_enter(",")

        self.W_write_reception_block_enter(";\n")

    def animation_block(self, animation):

        # animation.animation_index_dict
        self.W_write_reception_keyframe_start()

        if animation.animation_options["name"] in self.G_addeds_animation:
            self.W_write_reception_log_enter("{0}はすでに追加されているか、同じ名前のkeyframe-blackが存在するため追加生成が取り消されました".format(animation.animation_options["name"]))
            self.W_write_reception_keyframe_end()
            return

        self.W_write_reception_keyframe_enter("animationの生成順序{0}".format(len(self.GW_keyframe_queue)), comment=True)

        self.W_write_reception_keyframe_enter("@keyframes {0}".format(animation.animation_options["name"])+"{\n")
        for ail in animation.animation_index_list:

            return_val = self.specific_class_inspection(ail[2])

            self.W_write_reception_keyframe_enter("{0}{1}\n".format(ail[0], "% {"), indent=1)
            if return_val is None:
                self.W_write_reception_keyframe_enter("{0}:{1}{2};\n".format(ail[1], ail[2], ail[3]), indent=2)
            else:
                print("ail[3]", ail[3])
                if not ail[3] is None:
                    self.W_write_reception_keyframe_enter("{0}:{1}{2};\n".format(ail[1], return_val, ail[3]), indent=2)
                else:
                    self.W_write_reception_keyframe_enter("{0}:{1};\n".format(ail[1], return_val), indent=2)
            self.W_write_reception_keyframe_enter("}\n", indent=1)

        self.W_write_reception_keyframe_enter("}\n")
        self.W_write_reception_keyframe_end()

        self.G_addeds_animation.append(animation.animation_options["name"])
        self.W_write_reception_log_enter("{0}が生成されました".format(animation.animation_options["name"]))

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    # 特定のclassだった時にget_elementを引っ張ってくる

    def specific_class_inspection(self, class_data):
        type_class_data = type(class_data).__name__
        print("tt", type_class_data, self.G_specific_class_types)

        if type_class_data in self.G_specific_class_types:
            print("in", type_class_data)

            return class_data.get_element()

        return None
