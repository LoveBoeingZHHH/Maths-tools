class Rational1(object):
    def __init__(self):#初始化程序
        pass

    def gcd(a,b):#判断最大公约数
        if not a > b:
             a,b = b,a
        while b != 0 :
             remider = a%b
             a,b = b,remider
             print("%s" %a)
        return a

    def lcm(a,b):#返回最小公倍数
        lcm = a*b /Rational1.gcd(a,b)
        return lcm

class Rational(object):#以1/3,3/5为例，输出加法
    def __init__(self,numer,denom = 1):
        print("in constuctor")
        self.numer = numer
        self.deom = denom

    def __str__(self):
        print("in str")
        return str(self.numer) + "/" + str(self.deom)

    def __repr__(self):
        print("in repr")
        return self.__str__()

     #定义分数的加法
    def __add__(self, f):
        print(" in add")
        thelcm = int(Rational1.lcm(self.deom,f.deom))
        numeratorSum = int((thelcm/self.deom*self.numer)+(thelcm/f.deom*f.numer))
        return Rational(numeratorSum,thelcm)

     #定义分数的减法
    def __sub__(self, f):
        print("in sub")
        thelcm = Rational1.lcm(self.deom,f.deom)
        numeratorSub = (thelcm/self.deom*self.numer)-(thelcm/f.deom*f.numer)
        return Rational(numeratorSub,thelcm)

onehalf = Rational(1,3)
threefive = Rational(3,5)
thesum = onehalf + threefive
print(thesum)
