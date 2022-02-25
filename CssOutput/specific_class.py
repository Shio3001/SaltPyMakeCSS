from . import color
import abc
from . import specific_class_base

# get_elementはcssに挿入されるもの 適切に文字列を加工する必要がある
# ここにあるのは数値のフォーマット指定のためで、topやleftなどを直接指定してはならない(rotate3dはtransformに対してかかっている)
# specific(明確) 数値指定や要素を明確かつ固定化する 例えばカラーコードは16進数表記や10進数表記など様々な指定方法がある。
# この状態だと出力処理を阻害してしまうので#fffffなどの形式に統一したり
# marginなど順番が必要なものの順序を確保する目的がある

G_irection_text = ["X", "Y", "Z"]


class OmnidirectionalClass(specific_class_base.SpecificClassBase):  # marginなど4方向指定が必要なもの
    def __init__(self, top, right, bottom, left):
        self.index = {"top": top, "right": right, "bottom": bottom, "left": left}

    def get_element(self):
        # 順番の担保が必須なため
        joinlist = [self.index["top"], self.index["right"], self.index["bottom"], self.index["left"]]
        return_text = " ".join(joinlist)
        print(return_text)
        return return_text


class ColorClass(specific_class_base.SpecificClassBase):
    def __init__(self, colorcode):
        self.colorcode = colorcode

    def get_element(self):
        return self.colorcode


class RotateClass(specific_class_base.SpecificClassBase):
    def __init__(self, angle, direction="Z"):

        if not direction in G_irection_text:
            raise Exception("directionに設定された項目が不正です direction : {0}".format(direction))

        self.direction = direction
        self.angle = angle

    def get_element(self):
        numberdict = {"X": 0, "Y": 0, "Z": 0}
        numberdict[self.direction] = 1
        numberlist = list(numberdict.values())
        return_text = "rotate3d({0[0]}, {0[1]}, {0[2]}, {1})".format(numberlist, self.angle)
        return return_text


class PositionClass(specific_class_base.SpecificClassBase):
    def __init__(self, pos):
        self.pos = pos

    def get_element(self):
        return_text = str(self.pos)
        return return_text


class CircleClass(specific_class_base.SpecificClassBase):
    def __init__(self, shape_round=1):  # shape_round = 0 ~ 1の小数点の値で設定する
        self.border_radius = shape_round * 50

    def get_element(self):
        return_text = str(self.border_radius)
        return return_text


G_class_name_list = [
    "ColorClass",
    "OmnidirectionalClass",
    "RotateClass",
    "PositionClass",
    "CircleClass"
]  # export


# specific_class_base.RectangularCoordinateClass.__init__(self, xr, yr, zr)
# こんな感じで多重継承時に親へのinitがcss 系ます
