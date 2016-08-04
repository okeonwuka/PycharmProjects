# Exercise 4.4
# Standardize all letters to be drawn LEFT to RIGHT

import math


try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *



# Instantiate turtle world and turtle
world = TurtleWorld()
bob = Turtle()
# Speed turtle up
bob.delay = .1

# Primitive functions to be used:

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)

# polyline(bob, 2, 60, 60)
#
# arc(bob, 60, 180)


# Alphabets

# def draw_b(thing, radius):
#     arc(thing, radius, 180)
#     lt(thing, 180)
#     arc(thing, radius, 180)
#     lt(thing)
#     fd(thing, 4*radius)
#     lt(thing)

def draw_a(thing, radius):
    lt(thing, 180)
    arc(thing, radius, -180)
    rt(thing, 90)
    fd(thing, 2*radius)



def draw_b(thing, radius):
    arc(thing, radius, 180)
    rt(thing, 90)
    fd(thing, 2*radius)
    lt(thing, 180)
    fd(thing, 4*radius)


def draw_c(thing, radius):
    lt(thing, 180)
    arc(thing, radius, -180)



def draw_d(thing, radius):
    lt(thing, 180)
    arc(thing, radius, -180)
    lt(thing, 90)
    fd(thing, 2*radius)
    rt(thing, 180)
    fd(thing, 4*radius)


def draw_e(thing, radius):
    lt(thing, 180)
    arc(thing, radius, -180)
    arc(thing, radius/2, -180)
    fd(thing, radius)

def draw_f(thing, radius):
    lt(thing, 90)
    fd(thing, 2* radius)
    lt(thing, 90)
    fd(thing, radius/2)
    rt(thing, 180)
    fd(thing, radius)
    rt(thing, 180)
    fd(thing, radius/2)
    rt(thing, 90)
    fd(thing, radius)
    arc(thing, radius/2, -180)


def draw_g(thing, radius):
    lt(thing, 180)
    arc(thing, radius, -180)
    rt(thing, 90)
    fd(thing, 4*radius)
    arc(thing, radius/2, -180)


def draw_h(thing, radius):
    lt(thing, 90)
    fd(thing, 6*radius)
    rt(thing, 180)
    fd(thing, 6*radius)
    rt(thing, 180)
    fd(thing, 2*radius)
    arc(thing, radius, -180)
    fd(thing, 2*radius)


def draw_i(thing, radius):
    rt(thing, 90)
    fd(thing, radius)
    rt(thing, 180)
    fd(thing, 2*radius)

def draw_j(thing, radius):
    lt(thing, 90)
    fd(thing, 2*radius)
    rt(thing, 180)
    fd(thing, 2*radius)
    # rt(thing, 90)
    arc(thing, radius/2, -180)


def draw_k(thing, radius):
    lt(thing, 90)
    fd(thing, 3*radius)
    lt(thing, 180)
    fd(thing, 2*radius)
    lt(thing, 45)
    fd(thing, 1.4*radius)
    lt(thing, 180)
    fd(thing, 1.4*radius)
    rt(thing, 90)
    fd(thing, radius)

def draw_l(thing, radius):
    lt(thing, 90)
    fd(thing, 3*radius)
    lt(thing, 180)
    fd(thing, 3*radius)
    lt(thing, 90)
    fd(thing, radius)


def draw_m(thing, radius):
    for i in range(2):
        lt(thing, 90)
        fd(thing, 2*radius)
        arc(thing, radius, -180)
        fd(thing, 2*radius)
        lt(thing, 90)



def draw_n(thing, radius):
    lt(thing, 90)
    fd(thing, 2*radius)
    arc(thing, radius, -180)
    fd(thing, 2*radius)




def draw_o(thing, radius):
    lt(thing, 180)
    arc(thing, radius, -360)
    lt(thing, 180)


def draw_p(thing, radius):
    arc(thing, radius, 180)
    lt(thing, 90)
    fd(thing, 4*radius)



def draw_q(thing, radius):
    lt(thing, 180)
    arc(thing, radius, 180)
    lt(thing, 90)
    fd(thing, 2*radius)
    lt(thing, 180)
    fd(thing, 4*radius)


def draw_r(thing, radius):
    lt(thing, 90)
    fd(thing, 2*radius)
    arc(thing, radius, -135)


def draw_s(thing, radius):
    fd(thing, 0.5*radius)
    arc(thing, radius/2, 180)
    arc(thing, radius/2, -180)
    fd(thing, 0.5*radius)


def draw_t(thing, radius):
    lt(thing, 90)
    fd(thing, 3*radius)
    lt(thing, 180)
    fd(thing, 0.5*radius)
    lt(thing, 90)
    fd(thing, 0.5*radius)
    lt(thing, 180)
    fd(thing, radius)
    lt(thing, 180)
    fd(thing, 0.5*radius)
    rt(thing, 90)
    fd(thing, 3*radius)
    lt(thing, 90)
    arc(thing, radius/2, 45)




def draw_u(thing, radius):
    lt(thing, 90)
    fd(thing, 2*radius)
    rt(thing, 180)
    fd(thing, 2*radius)
    arc(thing, radius, 180)
    fd(thing, 2*radius)


def draw_v(thing, radius):
        lt(thing, 60)
        fd(thing, 1.4*radius)
        lt(thing, 180)
        fd(thing, 1.4*radius)
        rt(thing, 120)
        fd(thing, 1.4*radius)
        lt(thing, 180)
        fd(thing, 1.4*radius)
        lt(thing, 120)



def draw_x(thing, radius):
        lt(thing, 60)
        fd(thing, 1.4*radius)
        lt(thing, 180)
        fd(thing, 1.4*radius/2)
        rt(thing, 120)
        fd(thing, 1.4*radius/2)
        lt(thing, 180)
        fd(thing, 1.4*radius)



def draw_z(thing, radius):
    fd(thing, 1.4*radius)
    bk(thing, 1.4* radius)
    lt(thing, 30)
    fd(thing, 1.8*radius)
    rt(thing, 30)
    bk(thing, 1.4*radius)





def start_position(thing):
    lt(thing, 180)




# draw_t(bob, 30)
# move(bob, 100)
draw_a(bob, 30)
move(bob, 100)
start_position(bob)
draw_p(bob, 30)


wait_for_user()


# Investigate for Spiral
# def draw_e(thing, radius):
#     lt(thing, 180)
#     arc(thing, radius, -180)
#     arc(thing, 3*radius/2, -180)