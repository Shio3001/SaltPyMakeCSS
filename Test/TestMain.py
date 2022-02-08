
import copy
import make_css
import class_forprocess
import specific_class

main_class = class_forprocess.DATAforProcess(rootname="dango ")
test1 = class_forprocess.ShapeClass(block_name="mikan")
test1.add_index("height", 50, "px")
test1.add_index("width", 100, "px")
color1 = specific_class.ColorClass("#aa00bb")
test1.add_index("background-color", color1)
ani_test1 = class_forprocess.AnimationClass(animation_name="Sakana")
ani_test1.add_index(progress_time=0, key="width", val=100, units="px")
ani_test1.add_index(progress_time=100, key="width", val=50, units="px")
ani_test1.set_animation_options("delay", 20, "s")
test1.add_animation(ani_test1)
color1a = specific_class.ColorClass("#ff24bb")
color1b = specific_class.ColorClass("#0024ff")
ani_test2 = class_forprocess.AnimationClass(animation_name="Momiji")
ani_test2.add_index(progress_time=0, key="margin", val=100, units="px")
ani_test2.add_index(progress_time=100, key="margin", val=50, units="px")
ani_test2.add_index(progress_time=0, key="background-color", val=color1a)
ani_test2.add_index(progress_time=100, key="background-color", val=color1b)
print(ani_test2.get_animation_options())
ani_test2.set_animation_options("delay", 20, "s")
test1.add_animation(ani_test2)
test2 = class_forprocess.ShapeClass(block_name="ringo")
test2.add_index("height", 1000, "px")
color2 = specific_class.ColorClass("#ffffbb")
test2.add_index("background-color", color2)
main_class.add_Shapes(test1)
main_class.add_Shapes(test2)
make_css.processMain(main_class, "./")
