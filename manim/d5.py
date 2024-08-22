from manim import *
import math
# config.pixel_height = 2160
# config.pixel_width = 3840

# # Calculate the aspect ratio
# aspect_ratio = config.pixel_width / config.pixel_height

# # Set the desired frame height for a 16:9 aspect ratio (standard for 4K)
# config.frame_height = 9.0

# # Calculate the corresponding frame width
# config.frame_width = 16 * config.frame_height * aspect_ratio / 9

class DFTRTAnimation(MovingCameraScene):
    def construct(self):
        # Create circle with text
        circle = Circle(1.6, color=BLUE, fill_opacity=0.1)
        text = Text("Types of DFTRT", color=WHITE).scale(0.5).next_to(circle, DOWN)
        circle_with_text = VGroup(circle, text)

        # Position the circle with text at the center of the screen
        circle_with_text.move_to(ORIGIN)

        # Display the circle with text
        self.play(DrawBorderThenFill(circle_with_text), run_time=2.5)

        # Define the positions for the new circles with increased distance
        scaling_factor = 2  # Increase this value to increase the distance
        positions = [
            [1, 0, 0],    # Right
            [-1, 0, 0],   # Left
            [1 / math.sqrt(2), 1 / math.sqrt(2), 0],  # Up-right
            [-1 / math.sqrt(2), 1 / math.sqrt(2), 0], # Up-left
            [-1 / math.sqrt(2), -1 / math.sqrt(2), 0],  # Up-right
            [1 / math.sqrt(2), -1 / math.sqrt(2), 0] # Up-left
        ]

        # Scale the positions
        scaled_positions = [[pos[0] * scaling_factor, pos[1] * scaling_factor, pos[2]] for pos in positions]

        # Create new circles and lines
        labels = [
            "Direct form of DFRFT",
            "Improved sampling-type DFRFT",
            "Linear combination-type DFRFT",
            "Eigenvector decomposition-type DFRFT",
            "Group theory-type DFRFT",
            "Impulse train-type DFRFT"
        ]
        circles = []

        lines = []
        self.camera.frame.save_state()
        for pos, label_text in zip(scaled_positions, labels):
            # Calculate the position on the circumference of the circle
            start_point = circle_with_text.get_center()
            end_point = start_point + 3.5 * normalize(pos)

            line = Line(start_point, end_point, color=GOLD,stroke_opacity=0.4)
            lines.append(line)

            # Create new circle with the same radius as the original circle
            new_circle = Circle(radius=0.75 * circle.radius, color=RED,fill_opacity=0.1)
            new_circle.move_to(end_point)
            circles.append(new_circle)

            # Create and format label text
            label = Text(label_text, color=YELLOW, background_stroke_color=WHITE, background_stroke_width=1, font_size=8)
            label.move_to(new_circle)

            self.play(Write(label))

        # Animate the lines extending out from the center
        for line in lines:
            self.play(Create(line), run_time=0.5)

        # Animate the formation of new circles at the end of each line
        for circle in circles:
            self.play(TransformFromCopy(circle_with_text, circle), run_time=1)
            self.play(self.camera.frame.animate.set(width=circle.width * 2).move_to(circle), run_time=2)
            self.wait(0.3)
            self.play(Restore(self.camera.frame))

        self.wait(1)
