import copy
import imp
import traceback
import class_forprocess
import specific_class
import time

# 大域変数の先頭にはG_をつける(Global)

G_NG_TAGS = ["div", "body"]
G_NG_TAGS_Message = "不適切なブロック名が設定されました 使用禁止:" + " ".join(G_NG_TAGS)
# animationプロパティを使う

G_specific_class_types = specific_class.class_name_list

G_block_queue = []
G_keyframe_queue = []

G_DEBUG_MODE = True

G_outputfileName = 'sample.css'

outputfile = open(G_outputfileName, "w")
# ここが呼ばれる


def processMain(root_class, write_path):
    for roop_shape in root_class.Shapes:
        block(root_class, roop_shape)

    EndProcess()

# 終了処理


def EndProcess():
    outputfile.close()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def comment_process(text):
    return "/* " + text + " */\n"


def indent_process(text, indent):
    for i in range(indent):
        text = "   " + text
        print("indent_process", indent, text)
    return text


def write_reception_block_start():
    G_block_queue.append("")


def write_reception_keyframe_start():
    G_keyframe_queue.append("")


def write_reception_block_enter(text, comment=False, indent=0):
    text = indent_process(text, indent)
    if comment:
        text = comment_process(text)
    G_block_queue[-1] += text


def write_reception_keyframe_enter(text, comment=False, indent=0):
    text = indent_process(text, indent)
    if comment:
        text = comment_process(text)
    G_keyframe_queue[-1] += text


def write_reception_block_end():
    outputfile.write(G_block_queue[-1])


def write_reception_keyframe_end():
    outputfile.write(G_keyframe_queue[-1])


# * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def block(root_class, shape_data):

    write_reception_block_start()

    write_reception_block_enter("blockの生成順序{0}".format(len(G_block_queue)), comment=True)

    for roop_animation in shape_data.animations:

        animation_block(roop_animation)

    if len(root_class.scope) > 0:  # CSSセレクタの設定
        write_reception_block_enter("{0}>".format(root_class.scope))

    if shape_data.block_name in G_NG_TAGS:
        raise Exception(G_NG_TAGS_Message)

    write_reception_block_enter("{0}".format("."+shape_data.block_name)+"{\n")
    block_index_by_animation_options(shape_data.animations)
    block_index(shape_data)
    write_reception_block_enter("}\n")

    write_reception_block_end()


def block_index(shape_data):
    for k, v in zip(shape_data.shape_index_dict.keys(), shape_data.shape_index_dict.values()):
        return_val = specific_class_inspection(v[0])

        if return_val is None:
            write_reception_block_enter("{0} : {1}{2};\n".format(k, v[0], v[1]), indent=1)

        else:
            write_reception_block_enter("{0} : {1};\n".format(k, return_val), indent=1)

        print("kv", k, v, return_val)


def block_index_by_animation_options(shape_data_animations):

    if len(shape_data_animations) == 0:
        return

    write_reception_block_enter("animation:", indent=1)

    for roop, roop_animation in enumerate(shape_data_animations):
        options_values = roop_animation.animation_options.values()

        for ov in options_values:
            print(type(ov))
            if type(ov) is list:
                write_reception_block_enter(" {0}{1}".format(ov[0], ov[1]))
            else:
                write_reception_block_enter(" {0}".format(ov))

        if roop < len(shape_data_animations) - 1:
            print(roop, len(shape_data_animations)-1)
            write_reception_block_enter(",")

    write_reception_block_enter(";\n")


def animation_block(animation):

    # animation.animation_index_dict
    write_reception_keyframe_start()
    write_reception_keyframe_enter("animationの生成順序{0}".format(len(G_keyframe_queue)), comment=True)

    write_reception_keyframe_enter("@keyframes {0}".format(animation.animation_options["name"])+"{\n")
    for ail in animation.animation_index_list:

        return_val = specific_class_inspection(ail[2])

        write_reception_keyframe_enter("{0}{1}\n".format(ail[0], "% {"), indent=1)

        if return_val is None:
            write_reception_keyframe_enter("{0}:{1}{2};\n".format(ail[1], ail[2], ail[3]), indent=2)
        else:
            write_reception_keyframe_enter("{0}:{1};\n".format(ail[1], return_val), indent=2)
        write_reception_keyframe_enter("}\n", indent=1)

    write_reception_keyframe_enter("}\n")

    write_reception_keyframe_end()


def animation_progress():
    pass


def animation_index():
    pass

# * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def specific_class_inspection(class_data):
    type_class_data = type(class_data).__name__
    print("tt", type_class_data, G_specific_class_types)

    if type_class_data in G_specific_class_types:
        print("in", type_class_data)

        return class_data.get_element()

    return None
