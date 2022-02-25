
from . import template_class_base


class ImageClass(template_class_base.TemplateClassBase):
    def __init__(self):  # shape_round = 0 ~ 1の小数点の値で設定する

        background_size_types = ["contain", "cover", "auto"]
        self.syntaxs_fluctuation = {}
        self.syntaxs_fixed = {}

    def set_syntax_fluctuation(self, key, value):
        self.syntaxs_fluctuation[key] = value

    def set_syntax_fixed(self, key, value):
        self.syntaxs_fixed[key] = value

    def get_syntax_block(self):
        return

    def get_syntax_animation(self):
        return


G_class_name_list = [
    "ImageClass"
]  # export

# https://developer.mozilla.org/ja/docs/Web/CSS/background-size
