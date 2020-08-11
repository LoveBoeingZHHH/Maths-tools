import os
print("[Choose language] Chinese enter 1,English enter 2")
b = int(input())
def Chinese():
    print("计算圆的面积与周长输入1")
    print("计算时针与分针夹角输入2")
    print("约分输入3")
    print("计算两数最大公约数及最小公倍数输入4")
    print("计算分数加法输入5")

def English():
    print("Calculate the area of the circle with the circumference input 1.")
    print("Calculate the hour hand and minute clip angle input 2.")
    print("Reduction input 3.")
    print("Calculate the two maximum conventions and the minimum common multiple input 4.")
    print("Calculate the score addition input 5.")

if b == 2:
    English()

if b == 1:
    Chinese()

a = int(input())
def alpha():
    os.system("python 2.py")

def bravo():
    os.system("python 3.py")

def charlie():
    os.system("python 4.py")

def delta():
    os.system("python 5.py")

def echo():
    os.system("python 6.py")

if a == 1:
    alpha()

if a == 2:
    bravo()

if a == 3:
    charlie()

if a == 4:
    delta()

if a == 5:
    echo()