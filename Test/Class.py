import color


class ColorClass:
    def __init__(self, colorcode):
        self.colorcode = colorcode

    def GetColor(self):
        return self.colorcode


class AnimationClass:
    def __init__(self, animation_name):
        self.animation_index_list = []  # 配列を入れる (value,単位)

        self.animation_options = {
            "name": animation_name,
            "fill_mode": "backwards",
            "duration": [3, "s"],
            "iteration_count": "infinite",
            "timing_function": "ease",
            "delay": [0.5, "s"],
            "direction": "normal"
        }

    def add_index(self, progress_time, key, val, units):
        index_array = [progress_time, key, val, units]

        insert_point = 0
        for roop_aid in self.animation_index_list:
            if roop_aid[0] > progress_time:
                insert_point = roop_aid

        self.animation_index_list.insert(insert_point, index_array)


class ShapeClass:
    def __init__(self, block_name):
        self.block_name = block_name
        self.shape_index_dict = {}  # 配列を入れる (value,単位)
        self.animations = []  # index : AnimationClass

    def add_index(self, key, val, units):
        index_array = [val, units]
        self.shape_index_dict[key] = index_array

    def add_animation(self, animation_class):
        self.animations.append(animation_class)


class DATAforProcess:
    def __init__(self):
        self.div_size = [100, 100]
        self.background_color = "#ff00ff"
        self.scope = ".MakeCssDiv"
        self.Shapes = []

    def add_Shapes(self, shape_class):
        self.Shapes.append(shape_class)
