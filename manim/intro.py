from manim import *
# config.pixel_height = 2160
# config.pixel_width = 3840

# # Calculate the aspect ratio
# aspect_ratio = config.pixel_width / config.pixel_height

# # Set the desired frame height for a 16:9 aspect ratio (standard for 4K)
# config.frame_height = 9.0

# # Calculate the corresponding frame width
# config.frame_width = 16 * config.frame_height * aspect_ratio / 9
class HeadingExample(MovingCameraScene):
    def construct(self):
        # Create a heading text
        heading = Text("Fractional Fourier transform", font_size=48, color=DARK_BLUE,weight=BOLD)
        heading_outline = heading.copy()
        heading_outline.set_stroke(width=1.5, color=GOLD) 
        # Position the heading on the screen
        heading_outline.move_to(ORIGIN)
        displacement = 0.9 * UP
        heading_outline.move_to(ORIGIN)
        heading_outline.shift(0.9* UP)
        self.play(Write(heading_outline))
        self.play(heading_outline.animate.shift(displacement))
        # Display the heading
        self.wait()
        subheading=Text("A novel tool for signal processing",font_size=36,color=ORANGE).next_to(heading_outline,DOWN)
        subheading.set_stroke(width=0.75, color=WHITE) 
        self.play(Write(subheading))
        self.wait()
        p1=[0,0,0,0]
        name1=Text("Nitin Ram Sai G(2023112026)",font_size=30).move_to(2*DOWN)
        name2=Text("Manikya Pant(2023112024)",font_size=30).move_to(2*DOWN).next_to(name1.get_center(),DOWN)
        self.play(Write(name1),Write(name2))
        self.play(name2.animate.shift(RIGHT*5+DOWN*1.5),name1.animate.shift(RIGHT*5+DOWN*1.5))
        
