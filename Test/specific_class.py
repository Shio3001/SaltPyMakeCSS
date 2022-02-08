import color
import abc
import specific_class_base

# get_elementはcssに挿入されるもの 適切に文字列を加工する必要がある


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


class RotateClass(specific_class_base.SpecificClassBase, specific_class_base.RectangularCoordinateClass):
    def __init__(self, xr=0, yr=0, zr=0):
        super.__init__(xr, yr, zr)

    def get_element(self):
        return self.colorcode


class_name_list = [
    "ColorClass",
    "OmnidirectionalClass"
]  # export

# tet = RotateClass(100, 200, 300)
