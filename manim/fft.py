from manim import *

class FractionalFourierTransform(Scene):
    def construct(self):
        # Create heading
        heading = Text("Introduction to Fractional Fourier Transform", font_size=44, color=BLUE)
        heading.to_edge(UP)
        self.play(Write(heading))

        # Define LaTeX equation
        equation = MathTex(
            r"F^{a}[s(x_1)] = s(x) = \frac{e^{i(\pi/4-\pi/2)}}{\sqrt{2 \pi \sin(\alpha)}}",
            r"* e^{-\frac{i}{2} x^2 \cot(\alpha)}",
            r"* \int_{-\infty}^{\infty} e^{\frac{-ix_1^{2}\cot(\alpha)}{2}-\frac{-ix_1x}{\sin(\alpha)}}"
        ).scale(0.8)
        equation.set_color_by_tex_to_color_map({
            r"\alpha": YELLOW,
            r"x_1": GREEN,
            r"x": GREEN
        })
        equation.next_to(heading, DOWN, buff=1)
        self.play(FadeIn(equation))
        self.wait()
