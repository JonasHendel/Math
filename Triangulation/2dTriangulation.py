from manim import *

import math as m

class Triangulation(Scene):
  def construct(self):
      circle = Circle(radius=1.5, color=GREEN)
      circle1 = Circle(radius=1.5, color=GREEN)
      circle2 = Circle(radius=m.sqrt(2), color=BLUE)
      circle3 = Circle(radius=m.sqrt(2), color=YELLOW)

      dot = Dot().set_color(RED)

      dot1 = Dot()

      dot2 = Dot()

      dot3 = Dot()

      circle1.move_to(np.array([0, 1.5, 0]))
      circle2.move_to(np.array([1, -1, 0]))
      circle3.move_to(np.array([-1, 1, 0]))

      dot1.move_to(circle1.get_center())
      dot2.move_to(circle2.get_center())
      dot3.move_to(circle3.get_center())

      line1 = Line(circle1.get_center(), dot.get_center())
      line2 = Line(circle2.get_center(), dot.get_center())
      line3 = Line(circle3.get_center(), dot.get_center())

      dot.generate_target()
      dot.target.shift(np.array([0.5, 0, 0]))

      x=ValueTracker(0)
      y=ValueTracker(0)
      dot.add_updater(lambda z: z.set_x(x.get_value()))
      line1.add_updater(lambda z: z.become(Line(circle1.get_center(),dot.get_center())))
      line2.add_updater(lambda z: z.become(Line(circle2.get_center(),dot.get_center())))
      line3.add_updater(lambda z: z.become(Line(circle3.get_center(),dot.get_center())))

      # rad1 =  Text("Radius=1.5").to_corner(LEFT + UP).scale(0.7)
      # rad2 = Text("Radius=1.41421").next_to(rad1, direction=DOWN).scale(0.7)
      # rad3 = Text("Radius=1.41421").next_to(rad2, direction=DOWN).scale(0.7)

      self.play(GrowFromCenter(dot1), GrowFromCenter(dot2), GrowFromCenter(dot3))
      self.wait(4)
      self.play(GrowFromCenter(circle1), run_time=3) 
      self.wait(7)
      self.play(GrowFromCenter(circle2), run_time=3)
      self.wait(7)
      self.play(GrowFromCenter(circle3), run_time=3)
      self.wait(3)
      self.play(Create(line1), Create(line2), Create(line3))
      self.play(line1.animate.set_color(RED), line2.animate.set_color(RED), line3.animate.set_color(RED))
      self.play(GrowFromCenter(dot))
      self.wait(10)
      # self.play(MoveToTarget(dot), circle3.animate.scale(m.sqrt(26)/4), circle1.animate.scale(m.sqrt(10)/3), circle2.animate.scale(m.sqrt(10)/4))

      
      
      # self.play(GrowFromCenter(circle1), GrowFromCenter(circle2),GrowFromCenter(circle3))

