import cmath
import math


def rect_to_trig(z):
    r = abs(z)
    theta = cmath.phase(z)
    return r, theta
def trig_to_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return complex(x, y)
def rect_to_exp(z):
    r = abs(z)
    theta = cmath.phase(z)
    return r, theta
def exp_to_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return complex(x, y)