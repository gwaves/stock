#!/usr/bin/env python
from __future__ import division 
import struct
from ths_opt import ths_real, ths_time, ths_time_print
from pylab import *

f=open('600030.day','rb')
i=0
tag1=f.read(6)	#file header,not to much mean
str1=f.read(10)		#header info, include rec_num etc. 
rec_num,start_pos,rec_len,col_num=struct.unpack("i3h",str1) #one int, 3 short
print "record number is:",rec_num
print "data start position:%d;\trecord lenth:%d;\tcolom number:%d" %(start_pos,rec_len,col_num)
all_end = []
all_date = []
for i in range(0,rec_num):
	f.seek(start_pos+i*rec_len)
	str1=f.read(28)  #in echo record, only 28 info have meaning
	date,start,high,low,end,money,vol=struct.unpack("7i",str1) #7 int
	try:
		aver=ths_real(money)/ths_real(vol)	#some data have 0 vol for exsample "tingpai"
	except ZeroDivisionError:
	#	print "vol is zero"
		aver = 0
#	fmt_str="#%7.7d, time:%d:\tprice:%5.2f-%5.2f\trange:%5.2f-%5.2f, vol:%11d(%15d), aver:%5.2f"
#	print fmt_str%(i,date,ths_real(start),ths_real(end),ths_real(low),ths_real(high),ths_real(vol), ths_real(money),aver)
	all_end.append(ths_real(end))
	all_date.append(date-20140000)
x=np.linspace(1,rec_num,rec_num)
plot(all_date,all_end)
show()

