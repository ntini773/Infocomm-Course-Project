from manim import *

class HeadingExample(MovingCameraScene):
    def construct(self):
        # Create a heading text
        heading = Text("Fractional Fourier transform", font_size=48, color=DARK_BLUE, weight=BOLD)
        heading_outline = heading.copy()
        heading_outline.set_stroke(width=1.5, color=GOLD) 

        # Position the heading on the screen
        heading_outline.move_to(ORIGIN)
        displacement = 0.9 * UP
        heading_outline.move_to(ORIGIN)
        heading_outline.shift(0.9* UP)
        self.play(Write(heading_outline))
        self.play(self.camera.frame.scale, 0.5)
        self.wait()

        # Zoom into the heading
        self.play(self.camera.frame.move_to, heading_outline)

        # Display the heading
        self.wait()
        subheading = Text("A novel tool for signal processing", font_size=36, color=ORANGE).next_to(heading_outline, DOWN)
        subheading.set_stroke(width=0.75, color=WHITE) 
        self.play(Write(subheading))
        self.wait()

        # Write the equation
        equation = MathTex(r"\sin(x) = x").scale(1.5)
        equation.next_to(heading_outline, DOWN, buff=1)
        self.play(Write(equation))

        # Move the equation into view
        self.play(self.camera.frame.move_to, equation)

        # Write the names
        name1 = Text("Nitin Ram Sai G(2023112026)", font_size=30).move_to(2*DOWN)
        name2 = Text("Manikya Pant(2023112024)", font_size=30).move_to(2*DOWN).next_to(name1.get_center(), DOWN)
        self.play(Write(name1), Write(name2))
        self.play(name2.animate.shift(RIGHT*5+DOWN*1.5), name1.animate.shift(RIGHT*5+DOWN*1.5))
