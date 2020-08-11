
#coding=utf-8
 
import string

#输入小时分钟
hour = int(input("请输入小时："))
minute = int(input("请输入分钟："))

#使用12小时制
if hour>12:
    hour=hour-12
    
#计算夹角
minuteAngel = (float(minute)*360)/60
hourAngel = (float(hour)%12)*30 + (float(minute)*30)/60
 
angel = abs(hourAngel - minuteAngel)
if angel<=180:
    print ("夹角角度为：%.2f" %angel)
else:
    print("夹角角度为：%.2f" %(360-angel))
