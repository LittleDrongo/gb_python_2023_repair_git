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
