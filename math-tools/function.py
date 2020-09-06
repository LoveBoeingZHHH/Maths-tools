import string
import math
class time_angle:
    def time(hour,minute):
    #使用12小时制
    if hour>12:
        hour=hour-12
    minuteAngel = (float(minute)*360)/60
    hourAngel = (float(hour)%12)*30 + (float(minute)*30)/60
    angel = abs(hourAngel - minuteAngel)
    if angel<=180:
        print ("夹角角度为：%.2f" %angel)
    else:
        print("夹角角度为：%.2f" %(360-angel))

class circle_area:
    import math
    def circle(radius,value):
        circumference = 2*value*radius
        area = value*radius*radius
        print("circumference of circle: %.2f" %circumference)
        print("area of circle: %.2f" %area)

class a
