from manim import *
import numpy as np

class Star(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=(-9, 9),
            y_range=(-9, 9),
            axis_config={"color": BLUE},
        )

        # Number of points in the star
        num_points = 20
        
        # Generate points for the star shape around origin
        star_points = []
        for i in range(num_points):
            angle = i * 2 * np.pi / num_points
            if i % 2 == 0:
                radius = 2  # Long radius for outer points
            else:
                radius = 1  # Short radius for inner points
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            star_points.append((x, y, 0))

        # Draw the star shape around origin
        star_origin = Polygon(*star_points, stroke_width=2, stroke_color=WHITE, fill_opacity=0)

        origin_label = MathTex("Signal").next_to(star_origin, UP)

        # Define the location and angle for the second star
        point_location = np.array([3, 2, 0])  # Location for the star
        inclination_angle = np.pi / 4  # Angle of inclination (45 degrees)
        scale_factor = 0.5  # Scaling factor for the second star

        # Generate points for the second star shape
        star_points_transformed = []
        for point in star_points:
            point_np = np.array(point)
            rotated_point = self.rotate_vector(point_np * scale_factor, inclination_angle)
            translated_point = rotated_point + point_location
            star_points_transformed.append(translated_point)

        # Draw the second star shape
        star_transformed = Polygon(*star_points_transformed, stroke_width=2, stroke_color=WHITE, fill_opacity=0)

        transformed_label = MathTex("Noise").next_to(star_transformed, UP)

        # Label X-axis
        x_label = MathTex("x_{0} = t").next_to(axes.x_axis.get_end(), RIGHT)
        x_label.shift(1 * LEFT)
        x_label.shift(0.3 * DOWN)

        # Label Y-axis
        y_label = MathTex("x_{1} = f").next_to(axes.y_axis.get_end(), UP)

        # Draw a ray at 45 degrees with arrows in both directions
        ray_start = np.array([-4.5, -3, 0])
        ray_end = np.array([4.5, 3, 0])
        ray = Line(ray_start, ray_end, color=WHITE).add_tip(tip_length=0.15)

        # Label the line x_alpha
        label_x_alpha = MathTex("x_{\\alpha}").next_to(ray_end, RIGHT)

        # Calculate the bounding box of the first star
        x_min = min(star_points, key=lambda p: p[0])[0]
        x_max = max(star_points, key=lambda p: p[0])[0]
        y_min = min(star_points, key=lambda p: p[1])[1]
        y_max = max(star_points, key=lambda p: p[1])[1]

        # Calculate the center of the bounding box
        center_x = (x_min + x_max) / 2 + 0.1
        center_y = (y_min + y_max) / 2 - 0.9

        # Calculate the angle of the line
        line_angle = np.arctan2(ray_end[1] - ray_start[1], ray_end[0] - ray_start[0])

        # Calculate the dimensions of the rectangle
        rect_width = (x_max - x_min) * 2  # Decrease the width further
        rect_length = 1 * (x_max - x_min)  # Increase the length

        # Draw the rectangle perpendicular to the line with the line as its base
        rectangle = Rectangle(width=rect_width * 0.5, height=rect_length, color=WHITE, fill_opacity=0).move_to(
            (center_x, center_y + 1, 0)).rotate(line_angle - np.pi / 2)

        # Animation
        self.add(axes)
        self.wait()

        self.play(Create(star_origin), Write(origin_label), run_time=3)
        self.wait()

        self.play(Create(star_transformed), Write(transformed_label), run_time=3)
        self.wait()

        # Create a line at the initial position
        initial_line = Line(ray_start, ray_start, color=WHITE).add_tip(tip_length=0.15)
        self.play(Create(initial_line), run_time=3)
        self.wait()

        # Rotate the line around the origin
        self.play(Rotate(initial_line, angle=line_angle, about_point=ORIGIN), run_time=3)
        self.wait()

        # Make the line stable at the final position
        self.play(ReplacementTransform(initial_line, ray), run_time=3)
        self.wait()

        self.play(Write(x_label), Write(y_label), run_time=3)
        self.wait()

        self.play(Write(label_x_alpha), run_time=3)
        self.wait()

        self.play(Create(rectangle), run_time=3)
        self.wait(2)

    def rotate_vector(self, vector, angle):
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                    [np.sin(angle), np.cos(angle), 0],
                                    [0, 0, 1]])
        return np.dot(rotation_matrix, vector)