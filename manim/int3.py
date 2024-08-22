from manim import *

class IntuitionBehindFormula(MovingCameraScene):
    def construct(self):
        # Create heading
        heading = Text("Whats the Intuition behind FRFT?", font_size=40, color=ORANGE)
        heading.to_edge(UP)
        self.play(Write(heading))

        # Create formula and box
        formula1 = MathTex(r"F(\psi_n) = \lambda_n \psi_n").scale(1.2)
        formula1_box = SurroundingRectangle(formula1, buff=0.1)
        formula1_group = VGroup(formula1_box, formula1)
        formula1_group.move_to(UP*0.5)

        self.play(Create(formula1_box), Write(formula1))

        # Draw arrow from the formula1 box
        arrow1 = Arrow(formula1_box.get_bottom(), DOWN*2, buff=0.1)
        self.play(Create(arrow1))

        # Write text below the arrow
        text_below_arrow1 = Tex("where ", font_size=26).next_to(arrow1, DOWN)
        eigen_function_description1 = Tex(r"\(\psi_n\) is an eigen function of Fourier Transform").next_to(text_below_arrow1, DOWN)
        self.play(Write(text_below_arrow1), Write(eigen_function_description1))

        # Draw arrow from eigen function description
        arrow2 = Arrow(eigen_function_description1.get_bottom(), DOWN*3, buff=0.1)
        self.play(Create(arrow2))

        # Move camera downwards along with the arrow
        self.play(
            self.camera.frame.animate.move_to(DOWN*5),
            arrow2.animate.shift(DOWN*2)
        )

        # Write second equation and box
        formula2 = MathTex(r"F(t) = \sum_{n=1}^{\infty} A_n \psi_n").scale(1.2)
        formula2_box = SurroundingRectangle(formula2, buff=0.1)
        formula2_group = VGroup(formula2_box, formula2)
        formula2_group.next_to(arrow2, DOWN)

        # Draw arrow from the eigen function description to the second formula box
        arrow3 = Arrow(eigen_function_description1.get_bottom(), formula2_box.get_top(), buff=0.1)
        self.play(Create(arrow3))

        self.play(Create(formula2_box), Write(formula2))

        # Draw another arrow from eigen function description
        arrow4 = Arrow(eigen_function_description1.get_bottom(), DOWN*5, buff=0.1)
        self.play(Create(arrow4))

        # Move camera downwards along with the arrow
        self.play(
            self.camera.frame.animate.move_to(DOWN*9),
            arrow4.animate.shift(DOWN*4)
        )

        # Write third equation and box
        formula3 = MathTex(r"A_n = \int_{-\infty}^{\infty} F(t) \cdot \psi_n").scale(1.2)
        formula3_box = SurroundingRectangle(formula3, buff=0.1)
        formula3_group = VGroup(formula3_box, formula3)
        formula3_group.next_to(arrow4, DOWN)

        # Draw arrow from the eigen function description to the third formula box

        self.play(Create(formula3_box), Write(formula3))
        self.wait()
