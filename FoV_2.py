"""
Field of View (FoV) Calculations:

This script calculates the field of view (FoV) for a camera system based on given parameters such as focal length, working distance, sensor diagonal, and horizontal and vertical angles. The calculations involve determining the diagonal FoV angle and the physical dimensions of the FoV at a specified working distance.

Key Formulas Used:
Diagonal Field of View (FoV) Angle: The diagonal FoV angle is calculated using the sensor diagonal and the focal length. The formula is: [ \text{Diagonal FoV (in degrees)} = 2 \times \arctan\left(\frac{\text{sensor_diagonal}}{2 \times \text{focal_length}}\right) ] This formula uses the arctangent function to determine the angle from the sensor diagonal and focal length.

Physical Field of View at Working Distance: The physical dimensions of the FoV (width, height, and diagonal) at the working distance are calculated using the tangent function. The formulas are: [ \text{Physical width (or height)} = 2 \times \text{working_distance} \times \tan\left(\frac{\text{half_angle_in_radians}}{2}\right) ] Here, the angles (horizontal, vertical, and diagonal) are first converted to radians using the math.radians function.

Parameters:
focal_length: The focal length of the camera lens in millimeters.
working_distance: The distance from the camera to the subject in millimeters.
sensor_diagonal: The diagonal size of the camera sensor in millimeters.
horizontal_angle: The horizontal field of view angle in degrees.
vertical_angle: The vertical field of view angle in degrees.
Calculations:
Diagonal FoV Angle: The script calculates the diagonal FoV angle using the given sensor diagonal and focal length.

Horizontal and Vertical FoV: The script calculates the horizontal and vertical FoV dimensions at the specified working distance using the given horizontal and vertical angles.

Diagonal FoV: The script calculates the diagonal FoV dimension at the specified working distance using the computed diagonal FoV angle.

Output:
The script prints the calculated diagonal FoV angle and the physical dimensions of the FoV (horizontal, vertical, and diagonal) at the specified working distance.
"""

import math

# Given parameters
focal_length = 8         # in mm
working_distance = 800.0   # in mm (1 meter)
sensor_diagonal = 11.1      # in mm
horizontal_angle = 98.84     # in degrees
vertical_angle = 82.44       # in degrees

# 1) Compute the diagonal field of view (FoV) angle from the sensor diagonal and focal length
#    Diagonal FoV (in degrees) = 2 * arctan(sensor_diagonal / (2*focal_length))
diagonal_angle = 2.0 * \
    math.degrees(math.atan(sensor_diagonal / (2.0 * focal_length)))

# 2) Compute the physical field of view at the working distance
#    Physical width (or height) = 2 * working_distance * tan(half_angle_in_radians)
#    Note: Convert angles to radians using math.radians(angle_in_degrees)

# Horizontal FoV in mm at the subject plane
horizontal_fov_mm = 2.0 * working_distance * \
    math.tan(math.radians(horizontal_angle) / 2.0)

# Vertical FoV in mm at the subject plane
vertical_fov_mm = 2.0 * working_distance * \
    math.tan(math.radians(vertical_angle) / 2.0)

# Diagonal FoV in mm at the subject plane (computed from diagonal_angle)
diagonal_fov_mm = 2.0 * working_distance * \
    math.tan(math.radians(diagonal_angle) / 2.0)

# Print out the results
print(f"Calculated diagonal angle of view: {diagonal_angle:.2f} degrees")
print(f"Field of view at {working_distance:.0f} mm working distance:")
print(f"  Horizontal FoV: {horizontal_fov_mm:.2f} mm")
print(f"  Vertical FoV:   {vertical_fov_mm:.2f} mm")
print(f"  Diagonal FoV:   {diagonal_fov_mm:.2f} mm")
