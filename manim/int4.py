from manim import *

class TimeFrequencyPlane(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False}
        )

        # Label axes
        axes_labels = axes.get_axis_labels(x_label="Time", y_label="Frequency")

        # Create grid
        grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            background_line_style={"stroke_color": GREY, "stroke_width": 1, "stroke_opacity": 0.5}
        )

        # Add title
        title = Text("Time Frequency Plane").scale(1.2).to_edge(UP)

        # Add elements to scene
        self.add(title)

        # Animation: Title appearing
        self.play(FadeIn(title), run_time=1)

        # Animation: Title disappearing
        self.wait(1)
        self.play(FadeOut(title), run_time=1)

        # Animation: Axes, Axes labels, and Grid appearing
        self.play(Create(axes), Write(axes_labels), Create(grid), run_time=3)
        self.wait(1)

        # Add horizontal line
        horizontal_line = Line(start=axes.c2p(-8, 2), end=axes.c2p(8, 2), color=RED)

        # Animation: Horizontal line appearing
        self.play(Create(horizontal_line), run_time=1)

        # Label the original line
        label = MathTex("e^{j\\omega t_{0}}").next_to(horizontal_line, UP)

        # Animation: Label appearing
        self.play(Write(label), run_time=1)

        # Wait for 5 seconds
        self.wait(10)

        # Define the rotation point
        rotation_point = axes.c2p(3, 2)

        # Define the rotation angle
        rotation_angle = 90 * DEGREES

        # Rotate the original line to create the new vertical line
        self.play(Rotate(horizontal_line, rotation_angle, about_point=rotation_point), run_time=1)

        # Remove the original label
        self.remove(label)

        # Label the new line
        new_label = MathTex("\\delta(t-t_{0})").next_to(horizontal_line, RIGHT)

        # Animation: Label appearing
        self.play(Write(new_label), run_time=1)

        self.wait(5)

        self.remove(new_label)

        for i in range(16):
            new_line=Line(start=axes.c2p(-8+i,8),end=axes.c2p(-8+i,-8),color=GREEN)
            self.play(Create(new_line), run_time=1)
            
        self.wait(1) 

        # Dim the screen
        dimmer = Rectangle(width=config["frame_width"], height=config["frame_height"], color=BLACK, fill_opacity=0.7)
        self.add(dimmer)

        # Write the text
        text = Text("The set of all such parallel lines is the identity kernel", color=WHITE).scale(0.8)
        self.play(Write(text), run_time=2)

        self.wait(2)