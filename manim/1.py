from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height
# class IntroAnimation(Scene):
#     def construct(self):
#         # Title
#         title = Text("   Fractional Fourier transform: &A novel tool for signal processing", color=ORANGE,font_size=48).scale(1.5)
#         title.move_to(UP*2)
        
#         # Subheading
#         subheading_1 = Text("Nitin Ram Sai G(2023112026)", color=WHITE)
#         subheading_1.next_to(title, DOWN*4)
#         subheading_2 = Text("Manikya Pant(2023112024)", color=WHITE)
#         subheading_2.next_to(subheading_1, DOWN*4)
        
#         # Animation
#         self.play(Write(title))
#         self.wait(1)
#         self.play(Write(subheading_1))
#         self.play(Write(subheading_2))
#         self.wait(2)

class BEC(Scene):
    def construct(self):
      rx = Square().set_color(RED).to_edge(RIGHT, LARGE_BUFF)
      tx = Square().set_color(RED).to_edge(LEFT, LARGE_BUFF)
      RX = Text("receiver").next_to(rx, DOWN).scale(0.5)
      TX = Text("transmitter").next_to(tx, DOWN).scale(0.5)

      self.play(Create(rx), Create(tx), run_time=1)
      self.wait()
      self.play(Write(VGroup(RX,TX), run_time=2))
      self.wait()

      codewordTx = Text("1100 1000").shift(tx.get_center()).scale(0.5)
      codewordRx = Text("1?00 100?").shift(rx.get_center()).scale(0.5)
      self.play(ReplacementTransform(codewordTx, codewordRx, run_time = 3))
      self.wait()


      p1= [2,-2,0]
      p2= [-2,-2,0]
      p3= [2, 0, 0]
      p4= [-2,2,0] 
      p5= [2,2,0]
      bec = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
      self.play(Create(bec))

      self.play(Write(VGroup(Text("1").next_to(p2, LEFT).scale(0.5), Text("0").next_to(p4, LEFT).scale(0.5)), run_time = 1))
      self.wait( )
      self.play(Write(VGroup(Text("1").next_to(p1, RIGHT).scale(0.5), Text("?").next_to(p3, RIGHT).scale(0.5), Text("0"))))
      self.wait()
      self.play(Write(Text("Binary Erasure Channel").next_to(bec, DOWN).scale(0.5)))
      self.wait(3)