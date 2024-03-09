from big_ol_pile_of_manim_imports import *

class Mobjects(Scene):
    '''
    Examples of the mobjects available in the manim library.
    (manimlib/mobject)
    '''
    def construct(self):
        # TextMobject
        text_mobject = TextMobject("47463")
        self.play(Write(text_mobject))
        self.wait()
        self.play(FadeOut(text_mobject))
        
        # TexMobject
        tex_mobject = TextMobject("TexMobject")
        tex_mobject.shift(UP)
        formula = TexMobject("\sum_{k=0}^\\infty \\frac{c}{k^2} =  \\frac{8\\pi^2}{996}")
        formula.shift(UP)
        formula.next_to(tex_mobject, DOWN)
        self.play(Write(tex_mobject), Write(formula))
        self.wait()
        self.play(FadeOut(tex_mobject), FadeOut(formula))

        # number line
        number_line = NumberLine()
        number_line.add_numbers()
        self.play(ShowCreation(number_line, submobject_mode = "one_at_a_time"))
        
        number_line_text = TextMobject("NumberLine")
        number_line_text.shift(UP)
        self.play(Write(number_line_text))
        self.wait()
        self.play(FadeOut(number_line_text))
        self.play(FadeOut(number_line))

        # plane
        plane = NumberPlane()
        self.play(
            ShowCreation(plane, summobject_mode = "lagged_start")
        )
        plane_text = TextMobject("NumberPlane")
        plane_text.to_edge(UP)
        self.play(Write(plane_text))

        # vector
        vector = Vector([-2, 3])
        self.show_mobject("Vector", vector, GrowArrow, 
            shift=UP+2*LEFT)

        # dot
        self.show_mobject("Dot", Dot(radius = 0.1).set_color(RED),
            GrowFromCenter, shift=0.5*(UP+LEFT))

        self.show_mobject("Line", Line(ORIGIN, UP+2*RIGHT), ShowCreation,
            shift=1.5*(UP+0.5*RIGHT))

        graph = ParametricFunction(
            lambda t : 4*t*RIGHT + 2*smooth(t)*UP
        )
        graph_line = Line(graph.points[0], graph.points[-1], color = WHITE)
        graph_text = TextMobject("ParametricFunction")
        graph_text.next_to(graph, 0.5*UP+2*LEFT)
        
        self.play(ShowCreation(graph), Write(graph_text))
        self.play(Transform(graph, graph_line))
        self.play(Uncreate(graph), FadeOut(graph_text))

        self.play(FadeOut(plane_text))
        self.play(FadeOut(plane))


    def show_mobject(self, name, obj, animate, shift=None, text=None):
        if text is None:
            text = TextMobject(name)
        if shift is not None:
            text.shift(shift)
        self.play(animate(obj), Write(text))
        self.wait()

        if name == "Line":
            brace = Brace(obj)
            label = TextMobject("Brace").next_to(brace, DOWN).scale(0.7)

            self.play(GrowFromCenter(brace))
            self.play(Write(label))
            self.wait()
            self.play(Uncreate(label), FadeOut(brace), Uncreate(text), FadeOut(obj))
            return

        self.play(Uncreate(text), FadeOut(obj))
        self.wait()
