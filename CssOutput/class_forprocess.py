import uuid
import copy


class AnimationClass:
    def __init__(self, animation_name):
        self.animation_index_list = []  # 配列を入れる (value,単位)

        self.animation_options = {
            "name": animation_name,
            "fill_mode": "backwards",
            "duration": [5, "s"],
            "iteration_count": "infinite",
            "timing_function": "ease",
            "delay": [0, "s"],
            "direction": "normal"
        }

    def get_animation_options(self):
        return copy.deepcopy(self.animation_options)

    def set_animation_options(self, key, val, units=None):
        op_type = type(self.animation_options[key])

        if op_type is list:
            self.animation_options[key] = [val, units]
            return

        if op_type is str:
            self.animation_options[key] = str(val)
            return

    def add_index(self, progress_time, key, val, units=None):
        index_array = [progress_time, key, val, units]

        insert_point = 0
        for roop_aid in self.animation_index_list:
            if roop_aid[0] < progress_time:
                insert_point = roop_aid[0]

        print("insert_point", insert_point, progress_time)
        self.animation_index_list.insert(int(insert_point), index_array)


class ShapeClass:
    def __init__(self, block_name):
        self.block_name = block_name
        self.shape_index_dict = {}  # 配列を入れる (value,単位)
        self.animations = []  # index : AnimationClass

    def add_index(self, key, val, units=None):
        index_array = [val, units]
        self.shape_index_dict[key] = index_array

    def add_animation(self, animation_class):
        self.animations.append(animation_class)


class DATAforProcess:
    def __init__(self, rootname="MakeCssDiv"):
        self.div_size = [100, 100]
        self.background_color = "#ff00ff"

        self.scope = "." + rootname
        self.Shapes = []

    def add_Shapes(self, shape_class):
        self.Shapes.append(shape_class)
