print("输入分数（格式x/y,z/α)")
a = input()
b = a.split(',')
def alpha(a,b):
    if a < b:
        a,b = b,a
    r = 1
    while r != 0:
        r = a%b
        a = b
        b = r
    return a

num1 = b[0].split('/')
num2 = b[1].split('/')
sum1 = int(num1[0])*int(num2[1]) + int(num2[0])*int(num1[1])
sum2 = int(num1[1])*int(num2[1])
GCD = alpha(sum1,sum2)

c = int(sum1/GCD)
d = int(sum2/GCD)

if c%d == 0:
    print(int(c/d))
else:
    print(str(c)+ '/'+str(d))
