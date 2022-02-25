
import copy
from . import make_css
from . import class_forprocess
from . import specific_class

main_class = class_forprocess.DATAforProcess(rootname="dango")
test1 = class_forprocess.ShapeClass(block_name="mikan")
test1.add_index("height", 50, "px")
test1.add_index("width", 100, "px")
color1 = specific_class.ColorClass("#aa00bb")
test1.add_index("background-color", color1)
ani_test1 = class_forprocess.AnimationClass(animation_name="yodogawa")
# ani_test1.add_index(progress_time=0, key="width", val=100, units="px")
# ani_test1.add_index(progress_time=100, key="width", val=50, units="px")
ani_test1.set_animation_options("delay", 20, "s")
test1.add_animation(ani_test1)

rotate1a = specific_class.RotateClass(0, direction="Z")
rotate1b = specific_class.RotateClass(360, direction="Z")
test2 = class_forprocess.ShapeClass(block_name="ringo")
test2.add_index("height", 54636363, "px")
test2.add_index("width", 100, "px")

RINGO = specific_class.ColorClass("#cccccc")
test2.add_index("color", RINGO)

ani2_test1 = class_forprocess.AnimationClass(animation_name="cutrhnicurnhtiunhbcirxu")
ani2_test1.add_index(progress_time=0, key="transform", val=rotate1a, units="deg")
ani2_test1.add_index(progress_time=100, key="transform", val=rotate1b, units="deg")

pos1a = specific_class.PositionClass(0)
pos1b = specific_class.PositionClass(100)
pos1c = specific_class.PositionClass(0)
pos1d = specific_class.PositionClass(100)

round_shape1 = specific_class.CircleClass(0)
round_shape2 = specific_class.CircleClass(1)

color1a = specific_class.ColorClass("#ff24bb")
color1b = specific_class.ColorClass("#0024ff")
ani_test2 = class_forprocess.AnimationClass(animation_name="Momiji")
ani_test2.add_index(progress_time=0, key="background-color", val=color1a)
ani_test2.add_index(progress_time=100, key="background-color", val=color1b)
ani_test2.set_animation_options("delay", 20, "s")
test2.add_animation(ani_test2)

ani2_test2 = class_forprocess.AnimationClass(animation_name="hjiyjmyojmroi")
ani2_test2.add_index(progress_time=0, key="left", val=pos1a, units="px")
ani2_test2.add_index(progress_time=100, key="left", val=pos1b, units="px")
ani2_test2.add_index(progress_time=0, key="top", val=pos1c, units="px")
ani2_test2.add_index(progress_time=100, key="top", val=pos1d, units="px")
ani2_test2.add_index(progress_time=0, key="border-radius", val=round_shape1, units="%")
ani2_test2.add_index(progress_time=100, key="border-radius", val=round_shape2, units="%")

pos2a = specific_class.PositionClass(0)
pos2b = specific_class.PositionClass(100)

ani3_test1 = class_forprocess.AnimationClass(animation_name="shinbashi")
ani3_test1.add_index(progress_time=0, key="left", val=pos1a, units="%")
ani3_test1.add_index(progress_time=100, key="left", val=pos1b, units="%")

test1.add_animation(ani3_test1)

test2.add_animation(ani2_test2)

# test2.add_index("height", 1000, "px")
color2 = specific_class.ColorClass("#ffffbb")
test2.add_index("background-color", color2)
main_class.add_Shapes(test1)
main_class.add_Shapes(test2)

process = make_css.MakeCssClass()

process.processMain(main_class, "./")
