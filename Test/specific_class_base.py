import color
import abc

import copy


class SpecificClassBase(object, metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_element(self):
        pass


class RectangularCoordinateClass():  # 直交座標系,xyz指定する必要があるものに使う
    def __init__(self, x, y, z=None):
        self.index = {"x": x, "y": y, "z": z}

    def set_value(self, direction, value):
        if not direction in list(self.index.keys()):
            raise Exception("{0}が存在しません".format(direction))

        self.index[direction] = copy.deepcopy(value)
