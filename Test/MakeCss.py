import copy
import traceback

NG_TAGS = ["div", "body"]
NG_TAGS_Message = "不適切なブロック名が設定されました 使用禁止:" + " ".join(NG_TAGS)
# animationプロパティを使う


def process(root_class, write_path):
    outputfile = open('sample.css', "w")

    for roop_shape in root_class.Shapes:
        block(outputfile, root_class, roop_shape)


def block(file, root_class, shape_data):

    for roop_animation in shape_data.animations:
        animation_block(file, roop_animation)

    if len(root_class.scope) > 0:  # CSSセレクタの設定
        file.write("{0}>".format(root_class.scope))

    if shape_data.block_name in NG_TAGS:
        raise Exception(NG_TAGS_Message)

    file.write("{0}".format("."+shape_data.block_name)+"{\n")
    block_index_by_animation_options(file, shape_data.animations)
    block_index(file, shape_data)
    file.write("}\n")


def block_index(file, shape_data):
    for k, v in zip(shape_data.shape_index_dict.keys(), shape_data.shape_index_dict.values()):
        print(k, v)
        file.write("    {0} : {1}{2};\n".format(k, v[0], v[1]))


def block_index_by_animation_options(file, shape_data_animations):

    if len(shape_data_animations) == 0:
        return

    file.write("    animation:")

    for roop, roop_animation in enumerate(shape_data_animations):
        options_values = roop_animation.animation_options.values()

        for ov in options_values:
            print(type(ov))
            if type(ov) is list:
                file.write(" {0}{1}".format(ov[0], ov[1]))
            else:
                file.write(" {0}".format(ov))

        if roop < len(shape_data_animations) - 1:
            print(roop, len(shape_data_animations)-1)
            file.write(",")

    file.write(";\n")


def animation_block(file, animation):

    # animation.animation_index_dict

    file.write("@keyframes {0}".format(animation.animation_options["name"])+"{\n")
    for ail in animation.animation_index_list:
        file.write("    {0}{1}\n".format(ail[0], "% {"))
        file.write("        {0}:{1}{2};\n".format(ail[1], ail[2], ail[3]))
        file.write("    }\n")

    file.write("}\n")


def animation_progress():
    pass


def animation_index():
    pass
