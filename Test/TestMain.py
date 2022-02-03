
import copy
import MakeCss
import Class

main_class = Class.DATAforProcess()


test1 = Class.ShapeClass(block_name="mikan")
test1.add_index("height", 50, "px")

color1 = Class.ColorClass("#aa00bb")
print(color1)

if type(color1) is Class.ColorClass:
    print("gya")

test1.add_index("background-color", color1, "%")

ani_test1 = Class.AnimationClass(animation_name="Sakana")
ani_test1.add_index(progress_time=0, key="width", val=100, units="px")
ani_test1.add_index(progress_time=100, key="width", val=50, units="px")
test1.add_animation(ani_test1)

ani_test2 = Class.AnimationClass(animation_name="Momiji")
ani_test2.add_index(progress_time=43, key="width", val=52, units="px")
ani_test2.add_index(progress_time=100, key="width", val=50, units="px")
test1.add_animation(ani_test2)

test2 = Class.ShapeClass(block_name="ringo")
test2.add_index("height", 1000, "px")
test2.add_index("background-color", 100, "%")

main_class.add_Shapes(test1)
main_class.add_Shapes(test2)

MakeCss.process(main_class, "./")
