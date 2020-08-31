import area
import angle
from fraction import Rational1,Rational
import reduction
import emm
a = int(input())
def circle():
    print("Enter the radius")
    print("Enter the value")
    radius = float(input())
    value = float(input())
    area.circle(radius,value)

def time_angle():
    print("Input the hour")
    print("Input the minute")
    h = int(input())
    m = int(input())
    angle.time(h,m)

def plus_minus():
    oh = int(input())
    ohh = int(input())
    ohhh = int(input())
    ohhhh = int(input())
    onehalf = Rational(oh,ohh)
    threefive = Rational(ohhh,ohhhh)
    thesum = onehalf + threefive
    print(thesum)

def red():
    num = int(input("Input numerator"))
    deno = int(input("Input denominator"))
    reduction.frac(num,deno)

def some():
    number1 = int(input('输入第一个数：'))
    number2 = int(input('输入第二个数：'))
    emm.fun(number1,number2)

if a == 1:
    circle()
if a == 2:
    time_angle()
if a == 3:
    plus_minus()
if a == 4:
    red()
if a == 5:
    some()
