#!/usr/bin/env python
from __future__ import division #to divde int number in float
import struct
from ths_opt import ths_real, ths_time, ths_time_print
from pylab import *


f=open('000001.min','rb')
i=0
tag1=f.read(6)	#file header,not to much mean
str1=f.read(10)		#header info, include rec_num etc. 
rec_num,start_pos,rec_len,col_num=struct.unpack("i3h",str1) #one int, 3 short
print "record number is:",rec_num
print "data start position:%d;\trecord lenth:%d;\tcolom number:%d" %(start_pos,rec_len,col_num)
all_aver=[]
all_end=[]
for i in range(0,rec_num):
	f.seek(start_pos+i*rec_len)
	str1=f.read(28)  #in echo record, only 28 info have meaning
	date,start,high,low,end,money,vol=struct.unpack("7i",str1) #7 int
	rmoney=ths_real(money)
	rvol=ths_real(vol)
	try:
		aver=rmoney/rvol	#some data have 0 vol for exsample "tingpai"
	except ZeroDivisionError:
	#	print "vol is zero"
		aver = 0
	all_aver.append(aver)
	all_end.append(ths_real(end))
#	fmt_str="#%7.7d, time:%s:\tprice:%5.2f-%5.2f\trange:%5.2f-%5.2f, vol:%11d(%15d), aver:%5.2f"
#	print fmt_str%(i,ths_time_print(date),ths_real(start),ths_real(end),ths_real(low),ths_real(high),rvol, rmoney,aver)


x=np.linspace(0,100,100)
plot(x,all_aver[0:100],'r')
plot(x,all_end[0:100],'g')
show()
