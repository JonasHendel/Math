from typing_extensions import runtime
from manim import *

class Test(ThreeDScene):


    def construct(self):
        satSize = 0.1
        axes = ThreeDAxes()
        
        earth = ParametricSurface(
            lambda u, v: np.array([
                np.cos(u) * np.cos(v),
                np.cos(u) * np.sin(v),
                np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            fill_color='#29ABCA', checkerboard_colors=False, resolution=(15, 32), fill_opacity=0.5, stroke_width=0,  should_make_jagged=False,
        )
        sat1 = ParametricSurface(
            lambda u, v: np.array([
                satSize * np.cos(u) * np.cos(v),
                satSize * np.cos(u) * np.sin(v),
                satSize * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            fill_color='#F5FF2D', checkerboard_colors=False, resolution=(15, 32), fill_opacity=1, stroke_width=0,  should_make_jagged=False,
        )
        sat2 = ParametricSurface(
            lambda u, v: np.array([
                satSize * np.cos(u) * np.cos(v),
                satSize * np.cos(u) * np.sin(v),
                satSize * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            fill_color='#F5FF2D', checkerboard_colors=False, resolution=(15, 32), fill_opacity=1, stroke_width=0,  should_make_jagged=False,
        )
        sat3 = ParametricSurface(
            lambda u, v: np.array([
                satSize * np.cos(u) * np.cos(v),
                satSize * np.cos(u) * np.sin(v),
                satSize * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            fill_color='#F5FF2D', checkerboard_colors=False, resolution=(15, 32), fill_opacity=1, stroke_width=0,  should_make_jagged=False,
        )

        signal = ParametricSurface(
            lambda u, v: np.array([
                1 * np.cos(u) * np.cos(v),
                1 * np.cos(u) * np.sin(v),
                1 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            fill_color='#F5FF2D', checkerboard_colors=False, resolution=(15, 32), fill_opacity=0.5, stroke_width=0,  should_make_jagged=False,
        ) 

        signal.move_to(np.array([2, 0, 2]))
        sat1.move_to(np.array([0.8, 0, 0.8]))
        sat2.move_to(np.array([0, 0.8, 0.8]))
        sat3.move_to(np.array([0.8, 0.8, 0]))



        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=160 * DEGREES) 
        self.add(axes,earth, sat1, sat2, sat3)
        # self.play(ShrinkToCenter(sphere))
        # self.play(Create(sphere))
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(5)