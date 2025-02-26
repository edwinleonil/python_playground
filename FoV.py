import math


def calculate_fov_dimensions(focal_length, working_distance, sensor_diagonal, aspect_ratio):
    """
    Calculate the width and height of the field of view (FOV) using the sensor diagonal.

    :param focal_length: Focal length of the lens in millimeters
    :param working_distance: Distance from the lens to the object in millimeters
    :param sensor_diagonal: Diagonal size of the sensor in millimeters
    :param aspect_ratio: Aspect ratio of the sensor (width / height)
    :return: A tuple containing FOV width and FOV height in millimeters
    """
    # Calculate diagonal field of view (DFOV) in radians
    dfov = 2 * math.atan(sensor_diagonal / (2 * focal_length))

    # Calculate the diagonal length of the FOV at the working distance
    fov_diagonal = 2 * working_distance * math.tan(dfov / 2)

    # Calculate FOV width and height using aspect ratio
    fov_width = fov_diagonal / math.sqrt(1 + (1 / aspect_ratio) ** 2)
    fov_height = fov_width / aspect_ratio

    return fov_width, fov_height


# Example usage
# sensor_width = 35  # in millimeters
# sensor_height = 24  # in millimeters
# sensor_diagonal = math.sqrt(sensor_width**2 + sensor_height**2)

focal_length = 35  # in millimeters
working_distance = 1000  # in millimeters (1 meter)
sensor_diagonal = 31.1  # in millimeters (for a full-frame 35mm sensor)

# Typical full-frame aspect ratio (36mm width / 24mm height)
aspect_ratio = 16 / 9

fov_width, fov_height = calculate_fov_dimensions(
    focal_length, working_distance, sensor_diagonal, aspect_ratio)
print(f"FOV Width: {fov_width:.2f} mm")
print(f"FOV Height: {fov_height:.2f} mm")
