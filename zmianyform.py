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


def format_trigonometric(r, theta):
    theta_deg = math.degrees(theta)
    return f"{r:.3f} (cos {theta_deg:.3f}° + i sin {theta_deg:.3f}°)"


def format_exponential(r, theta):
    theta_deg = math.degrees(theta)
    return f"{r:.3f} e^(i{theta_deg:.3f}°)"


def trigonometric_to_exponential(r, theta):
    return format_exponential(r, theta)


def exponential_to_trigonometric(r, theta):
    return format_trigonometric(r, theta)