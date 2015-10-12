# CodeSkulptor runs Python programs in your browser.

# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.

# Some features may work in other browsers, but do not expect

# full functionality.  It does NOT run in Internet Explorer.

def do_stuff():

    print "Hello world"

    return "Is it over yet?"

    print "Goodbye cruel world!"

    

print do_stuff()

n = 1024

print (n % 100 - n % 10) / 10

#f(x) = -5 x5 + 69 x2 - 47 

def f(x):

    return -5 * (x ** 5) + 69 * (x ** 2) - 47

print f(0)

print f(1)

print f(2)

print f(3)

print f(4)

print f(5)

def future_value(present_value, annual_rate, periods_per_year, years):

    rate_per_period = annual_rate / periods_per_year

    periods = periods_per_year * years

    

    # Put your code here.

    return present_value * ((1 + rate_per_period) ** periods)

    

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print future_value(500, .04, 10, 10)

#¼ n s2 / tan(π/n). 

print 5 / 4.0

import math

def area(n,s):

    return 1.0 / 4.0 * n * (s ** 2) / math.tan(math.pi / n)

print area(7.0,3.0)

def project_to_distance(point_x, point_y, distance):

    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    

    scale = distance / dist_to_origin

    print point_x * scale, point_y * scale

    

project_to_distance(2, 7, 4)

