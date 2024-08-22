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
        self.wait(2)

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
        self.wait(2)

        # Draw arrow from the eigen function description to the second formula box
        arrow3 = Arrow(eigen_function_description1.get_bottom(), formula2_box.get_top(), buff=0.1)
        self.play(Create(arrow3))

        self.play(Create(formula2_box), Write(formula2))

        # Draw another arrow from eigen function description
        arrow4 = Arrow(formula2_box.get_bottom(), DOWN*9, buff=0.1)
        self.play(Create(arrow4))
        self.play(
            self.camera.frame.animate.move_to(DOWN*9),
        )

        # Move camera downwards along with the arrow

        # Write third equation and box
        formula3 = MathTex(r"A_n = \int_{-\infty}^{\infty} F(t) \cdot \psi_n").scale(1.2)
        formula3_box = SurroundingRectangle(formula3, buff=0.1)
        formula3_group = VGroup(formula3_box, formula3)
        formula3_group.next_to(arrow4, DOWN)
        arrow5 = Arrow(formula3_box.get_bottom(), DOWN*14, buff=0.1)
        self.wait(2)
        

        # Draw arrow from the eigen function description to the third formula box

        self.play(Create(formula3_box), Write(formula3))
        self.wait()
        self.play(Create(arrow5))
        self.play(
            self.camera.frame.animate.move_to(DOWN*18),
        )
        formula4 = MathTex(r"M=V^{-1}DV ~~~~\therefore M^{\alpha}=V^{-1}D^{\alpha}V").scale(1.2)
        formula4_box = SurroundingRectangle(formula4, buff=0.1)
        formula4_group = VGroup(formula4_box, formula4)
        formula4_group.next_to(arrow5, DOWN)
        arrow6 = Arrow(formula4_box.get_bottom(), DOWN*20, buff=0.1)
        self.wait(2)
        

        # Draw arrow from the eigen function description to the third formula box

        self.play(Create(formula4_box), Write(formula4))
        self.wait()
        self.play(Create(arrow6))
        self.play(
            self.camera.frame.animate.move_to(DOWN*23),
        )
        formula5 = MathTex(r"F^{\alpha}\left\{ F(t)\right\}=\sum \left [ \int_{-\infty}^{\infty}F(t)\psi_n(t)dt.\lambda_n^{\alpha}.\psi_n(u) \right ]").scale(1.2)
        formula5_box = SurroundingRectangle(formula5, buff=0.1)
        formula5_group = VGroup(formula5_box, formula5)
        formula5_group.next_to(arrow6, DOWN)
        arrow7 = Arrow(formula5_box.get_bottom(), DOWN*25, buff=0.1)
        self.wait(2)
        

        # Draw arrow from the eigen function description to the third formula box

        self.play(Create(formula5_box), Write(formula5))
        self.wait()
        self.play(Create(arrow7))
        self.play(
            self.camera.frame.animate.move_to(DOWN*29),
        )
        formula6 = MathTex(r"F^{\alpha}\left\{ F(t)\right\}=\int_{-\infty}^{\infty}F(t).\left [ \sum_{1}^{\infty} \lambda_n^{\alpha}.\psi_n(t).psi_n(u)\right ].dt").scale(1.2)
        formula6_box = SurroundingRectangle(formula6, buff=0.1)
        formula6_group = VGroup(formula6_box, formula6)
        formula6_group.next_to(arrow7, DOWN)
        arrow8 = Arrow(formula6_box.get_bottom(), DOWN*30, buff=0.1)
        self.wait(2)
        

        # Draw arrow from the eigen function description to the third formula box

        self.play(Create(formula6_box), Write(formula6))
        self.wait()
        self.play(Create(arrow8))
        self.play(
            self.camera.frame.animate.move_to(DOWN*32),
        )
        text_below_arrow8 = Tex("where ", font_size=26).next_to(arrow8, DOWN)
        eigen_function_description8 = Tex(r" \(\sum_{1}^{\infty} \lambda_n^{\alpha}.\psi_n(t).psi_n(u)\) is called Transformation Kernel ").next_to(text_below_arrow8, DOWN)
        self.play(Write(text_below_arrow8), Write(eigen_function_description8))
        self.wait(2)
        t2=Tex("which is usually difficult to compute!! :( ",color=RED).next_to(eigen_function_description8,DOWN)
        t2_box = SurroundingRectangle(t2, buff=0.1,color=YELLOW,fill_opacity=0.2)
        self.play(Write(t2),Create(t2_box))

        self.wait(2)
