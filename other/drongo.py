import math

RAD = 360
USSR = 6000
NATO = 6400


# Вспомогательные методы

def convert_angle(value, input_angle, output_angle):
    return value / input_angle * output_angle


def deg_to_rad(degrees):
    radians = (math.pi / 180.0 * degrees)
    return radians


def distance_to_topographic(distance, angle_target):
    distance_topographic = math.cos(deg_to_rad(angle_target)) * distance
    return distance_topographic


# Основные методы

def get_direction(x_position, y_position, x_target, y_target):
    if x_target - x_position > 0 and y_target - y_position >= 0:
        result = abs(math.atan((y_target - y_position) / (x_target - x_position)))
    elif x_target - x_position < 0 and y_target - y_position >= 0:
        result = math.pi - abs(math.atan((y_target - y_position) / (x_target - x_position)))
    elif x_target - x_position < 0 and y_target - y_position < 0:
        result = math.pi + abs(math.atan((y_target - y_position) / (x_target - x_position)))
    else:
        result = 2 * math.pi - abs(math.atan((y_target - y_position) / (x_target - x_position)))
    result = result * 180 / math.pi
    return result


def get_distance(x_position, y_position, x_target, y_target):
    return math.sqrt(math.pow(x_position - x_target, 2) + math.pow(y_position - y_target, 2))


def get_angle_place(x_position, y_position, z_position, x_target, y_target, z_target):
    distance = get_distance(x_position, y_position, x_target, y_target)
    z_difference = z_target - z_position
    horizontal_distance = math.sqrt(math.pow(distance, 2) - math.pow(z_difference, 2))
    angle_radians = math.atan(z_difference / horizontal_distance)
    angle_degrees = angle_radians * (180.0 / math.pi)
    return angle_degrees


def get_direction_on_position(position, target):
    return get_direction(position[0], position[1], target[0], target[1])


def get_distance_on_position(position, target):
    return get_distance(position[0], position[1], target[0], target[1])


def get_angle_on_position(position, target):
    return get_angle_place(position[0], position[1], position[2], target[0], target[1], target[2])


def get_anglemeter(target_dir, tip_point_dir, mils):
    anglemeter = target_dir - tip_point_dir + (mils / 2)
    if anglemeter < 0:
        anglemeter += mils
    if anglemeter > mils:
        anglemeter -= mils
    return anglemeter


def get_tip_point(main_dir, anglemeter, mils):
    tip_point = main_dir - anglemeter + (mils / 2)
    if tip_point < 0:
        tip_point += mils
    if tip_point > mils:
        tip_point -= mils
    return tip_point


def get_next_tip_point(tip_point_dir, old_anglemeter, new_anglemeter, mils):
    off_set = old_anglemeter - new_anglemeter
    tip_point_dir += off_set
    if tip_point_dir > mils:
        tip_point_dir -= mils
    if tip_point_dir < 0:
        tip_point_dir += mils
    return tip_point_dir


def get_distance_angular_method(object_size_meters, angular_size_degrees):
    return object_size_meters / math.tan(deg_to_rad(angular_size_degrees))


# Создание позиций

def create_position(x, y, z):
    return [x, y, z]


def copy_position(position):
    return position.copy()


def edit_position(position, x, y, z):
    position[0] = x
    position[1] = y
    position[2] = z


def clear_position(position):
    position[0] = 0
    position[1] = 0
    position[2] = 0


# Поиск позиции

def find_position_2d(position, azimuth, distance):
    x_position, y_position = position[0], position[1]
    x_target = math.cos(deg_to_rad(azimuth)) * distance + x_position
    y_target = math.sin(deg_to_rad(azimuth)) * distance + y_position
    return [x_target, y_target]


def find_position_3d(position, azimuth, distance, angle_target):
    x_position, y_position, z_position = position[0], position[1], position[2]
    x_target = math.cos(deg_to_rad(azimuth)) * distance_to_topographic(distance, angle_target) + x_position
    y_target = math.sin(deg_to_rad(azimuth)) * distance_to_topographic(distance, angle_target) + y_position
    z_target = math.cos(deg_to_rad(angle_target - 90)) * distance + z_position
    return [x_target, y_target, z_target]


def find_cross_view_position(spotter_one, spotter_two, mil_system_one, dir_one, mil_system_two, dir_two):
    x_spotter_one, y_spotter_one = spotter_one[0], spotter_one[1]
    x_spotter_two, y_spotter_two = spotter_two[0], spotter_two[1]
    x_target = (y_spotter_two - math.tan(deg_to_rad(dir_two / mil_system_two * RAD)) * x_spotter_two -
                (y_spotter_one - math.tan(deg_to_rad(dir_one / mil_system_one * RAD)) * x_spotter_one)) / (
                           math.tan(deg_to_rad(dir_one / mil_system_one * RAD)) -
                           math.tan(deg_to_rad(dir_two / mil_system_two * RAD)))

    y_target = math.tan(deg_to_rad(dir_one / mil_system_one * RAD)) * x_target + (
            y_spotter_one - math.tan(deg_to_rad(dir_one / mil_system_one * RAD)) * x_spotter_one) if math.tan(
        deg_to_rad(dir_one / mil_system_one * RAD)) * x_target + (
            y_spotter_one - math.tan(deg_to_rad(dir_one / mil_system_one * RAD)) * x_spotter_one) == math.tan(
        deg_to_rad(dir_two / mil_system_two * RAD)) else math.tan(deg_to_rad(dir_one / mil_system_one * RAD)) * x_target + (
            y_spotter_one - math.tan(deg_to_rad(dir_one / mil_system_one * RAD)) * x_spotter_one)

    return [x_target, y_target]


def find_with_landmark(spotter, reaper, overshoot, deviation, angle_target, mil_system):
    angle_deg = get_angle_on_position(spotter, reaper)
    azimuth = get_direction_on_position(spotter, reaper)
    distance = get_distance_on_position(spotter, reaper)

    target = find_position_3d(
        spotter, azimuth + convert_angle(deviation, mil_system, RAD),
        distance + overshoot,
        angle_deg + convert_angle(angle_target, mil_system, RAD))

    return target


# Корректировка позиции

def rectangle_correct(position, x_position, y_position):
    position[0] += x_position
    position[1] += y_position


def pollar_correction(spotter, target, overshoot, deviation, mil_system):
    x_spotter, y_spotter, z_spotter = spotter[0], spotter[1], spotter[2]
    x_target, y_target, z_target = target[0], target[1], target[2]

    azimuth_target = get_direction(x_spotter, y_spotter, x_target, y_target)
    distance_target = get_distance(x_spotter, y_spotter, x_target, y_target)

    notch = find_position_2d(
        spotter,
        azimuth=azimuth_target - (deviation / mil_system * RAD),
        distance=distance_target - overshoot
    )

    x_notch, y_notch = notch[0], notch[1]

    target[0] = x_notch
    target[1] = y_notch
    target[2] = z_target


def burst_correction(target, brust):
    x_diff = target[0] - brust[0]
    y_diff = target[1] - brust[1]

    rectangle_correct(target, x_diff, y_diff)


def cross_view_correction(target, spotter_one, spotter_two, mil_system_one, mil_system_two, deviation_one, deviation_two):
    dir_one = get_direction_on_position(spotter_one, target)
    dir_two = get_direction_on_position(spotter_two, target)
    target = find_cross_view_position(
        spotter_one=spotter_one, mil_system_one=RAD,
        spotter_two=spotter_two, mil_system_two=RAD,
        dir_one=dir_one - convert_angle(deviation_one, USSR, RAD),
        dir_two=dir_two - convert_angle(deviation_two, USSR, RAD)
    )


# Консольные методы

def print_position_line(position):
    print(f"[{round(position[0], 0)}, {round(position[1], 0)}, {round(position[2], 0)}]")


def print_position_row(position):
    print(f"X: {round(position[0], 0)}")
    print(f"Y: {round(position[1], 0)}")
    print(f"Z: {round(position[2], 0)}")


def difference_positions(true_position, checked_position):
    x_true_pos, y_true_pos, z_true_pos = true_position[0], true_position[1], true_position[2]
    x_check_pos, y_check_pos, z_check_pos = checked_position[0], checked_position[1], checked_position[2]

    x_res_proc = (1 - (x_true_pos / x_check_pos)) * 100
    y_res_proc = (1 - (y_true_pos / y_check_pos)) * 100
    z_res_proc = (1 - (z_true_pos / z_check_pos)) * 100

    print("Отклонение от позиций")
    print(f"X: {round((x_true_pos - x_check_pos), 2):6} м. | {round(x_res_proc, 2):6}%")
    print(f"Y: {round((y_true_pos - y_check_pos), 2):6} м. | {round(y_res_proc, 2):6}%")
    print(f"Z: {round((z_true_pos - z_check_pos), 2):6} м. | {round(z_res_proc, 2):6}%")