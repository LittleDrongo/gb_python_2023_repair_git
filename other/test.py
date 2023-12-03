from drongo import *


position = create_position(14430, 1390, 467)
spotter = create_position(10160, 4880, 302)
target2 = create_position(15040, 1670, 0)

target = find_position_3d(spotter, 45, 1900, 0)
print(target)

print(
    get_distance_on_position(position,target2)
)

print(
    convert_angle(
        get_direction_on_position(position, target2), RAD, USSR
    )
)


target3 = find_position_3d(position = spotter, 
                           azimuth =  convert_angle(45, USSR, RAD), 
                           distance = 1900, 
                           angle_target = convert_angle(10, USSR, RAD)
                           )

print(F"Цель 3{target3}")


# Ожидаемый ответ:

# 1 2 3 4
# 2 4 5 6
# 3 5 6 7
# 4 6 7 8

# Ваш ответ:

# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8

