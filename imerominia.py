#  program to show calendar 

import datetime
import calendar
yy = int(input("Enter a year: "))
mm = int(input("Enter a month: "))
gvr = datetime.date(yy,mm,4)
print(gvr.strftime("%B %Y"))
print("S  M  T  W  T  F  S" )
array=([[ 1, 2  , 3 ,4  , 5 , 6,7],
       [ 8,  9,  10,  11,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
print array

print(calendar.month(yy, mm))

		
