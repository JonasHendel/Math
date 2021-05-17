from manim import *

import math as m

class Triangulation(ThreeDScene):
  def construct(self):
    earth = Sphere(
      radius=1, v_max=TAU, u_min=-PI, u_max=PI,
      fill_color='#1AFF2D', checkerboard_colors=False, resolution=(15, 32)
    )

    sat1 = Sphere(
      radius=0.1, v_max=TAU, u_min=-PI, u_max=PI,
      fill_color='#1AFF2D', checkerboard_colors=False, resolution=(15, 32)
    )

    sat1.move_to(np.array([1, 1, 0]))






    self.set_camera_orientation(phi=75 * DEGREES, theta=160 * DEGREES)
    self.add(earth, sat1)