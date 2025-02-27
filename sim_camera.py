import math
from panda3d.core import Point3, LineSegs, TextNode, GeomNode, CardMaker
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from FoV import calculate_fov_dimensions


class CameraProjectionApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Enable mouse control for the camera
        self.disable_mouse()
        self.camera.set_pos(0, -10, 0)
        self.camera.look_at(0, 0, 0)
        self.task_mgr.add(self.spin_camera_task, "SpinCameraTask")

        # Camera parameters
        focal_length = 35  # in millimeters
        working_distance = 1000  # in millimeters (1 meter)
        sensor_diagonal = 31.1  # in millimeters (for a full-frame 35mm sensor)
        aspect_ratio = 16 / 9

        # Calculate FOV dimensions
        fov_width, fov_height = calculate_fov_dimensions(
            focal_length, working_distance, sensor_diagonal, aspect_ratio)

        # Convert FOV dimensions to meters for Panda3D
        fov_width_m = fov_width / 1000
        fov_height_m = fov_height / 1000

        # Create a visual representation of the FOV
        self.draw_fov(fov_width_m, fov_height_m)

        # Create a box to represent the camera
        self.create_camera_representation()

    def draw_fov(self, width, height):
        # Create a LineSegs object to draw lines
        lines = LineSegs()
        lines.set_color(1, 0, 0, 1)  # Red color

        # Define the four corners of the FOV rectangle
        top_left = Point3(-width / 2, 1, height / 2)
        top_right = Point3(width / 2, 1, height / 2)
        bottom_left = Point3(-width / 2, 1, -height / 2)
        bottom_right = Point3(width / 2, 1, -height / 2)

        # Draw the rectangle
        lines.move_to(top_left)
        lines.draw_to(top_right)
        lines.draw_to(bottom_right)
        lines.draw_to(bottom_left)
        lines.draw_to(top_left)

        # Draw projection lines from the camera position to the corners of the FOV
        camera_position = Point3(0, 0, 0)
        lines.move_to(camera_position)
        lines.draw_to(top_left)
        lines.move_to(camera_position)
        lines.draw_to(top_right)
        lines.move_to(camera_position)
        lines.draw_to(bottom_left)
        lines.move_to(camera_position)
        lines.draw_to(bottom_right)

        # Draw X and Y axes
        lines.set_color(0, 1, 0, 1)  # Green color for axes
        lines.move_to(Point3(-width / 2, 1, 0))
        lines.draw_to(Point3(width / 2, 1, 0))  # X axis
        lines.move_to(Point3(0, 1, -height / 2))
        lines.draw_to(Point3(0, 1, height / 2))  # Y axis

        # Create tick marks and labels for X axis
        for i in range(int(-width / 2), int(width / 2) + 1):
            lines.move_to(Point3(i, 1, -0.1))
            lines.draw_to(Point3(i, 1, 0.1))
            self.create_text(str(i), Point3(i, 1, -0.2))

        # Create tick marks and labels for Y axis
        for i in range(int(-height / 2), int(height / 2) + 1):
            lines.move_to(Point3(-0.1, 1, i))
            lines.draw_to(Point3(0.1, 1, i))
            self.create_text(str(i), Point3(-0.2, 1, i))

        # Create a NodePath from the LineSegs object and attach it to the render
        fov_node = lines.create()
        self.render.attach_new_node(fov_node)

    def create_text(self, text, position):
        text_node = TextNode('node')
        text_node.set_text(text)
        text_node_path = self.render.attach_new_node(text_node)
        text_node_path.set_pos(position)
        text_node_path.set_scale(0.2)

    def create_camera_representation(self):
        # Create a simple box to represent the camera
        cm = CardMaker('camera_representation')
        cm.set_frame(-0.1, 0.1, -0.1, 0.1)
        camera_representation = self.render.attach_new_node(cm.generate())
        camera_representation.set_pos(0, 0, 0)
        camera_representation.set_color(
            0, 0, 1, 1)  # Blue color for the camera

    def spin_camera_task(self, task):
        angle_degrees = task.time * 6.0
        angle_radians = angle_degrees * (math.pi / 180.0)
        self.camera.set_pos(10 * math.sin(angle_radians), -
                            10 * math.cos(angle_radians), 3)
        self.camera.look_at(0, 0, 0)
        return task.cont


if __name__ == "__main__":
    app = CameraProjectionApp()
    app.run()
