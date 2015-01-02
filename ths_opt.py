#!/usr/bin/env python

def ths_real(input):
	sign_flag=input>>31 #sign_flag, if eq 0,positive, else negative
	if sign_flag == 0:
		sign_flag = 1
	else:
		sign_flag = -1
	factor=input>>28&0x7 #in highest 4bit, lower 3bit is 10**factor
	K=input&0xfffffff	#lowest 28bit is a real number
	real=K*(10**(sign_flag*factor))
	return real

def ths_time_print(input):
	min=input&0x3f
	hour=input>>6&0x1f
	day=input>>11&0x1f
	mon=input>>16&0xf
	year=(input>>20&0xfff)+1900
	str='%d-%d-%d-%d:%d'%(year,mon,day,hour,min)
	return str

def ths_time(input):
	min=input&0x3f
	hour=input>>6&0x1f
	day=input>>11&0x1f
	mon=input>>16&0xf
	year=input>>20&0xfff+1900
	return year,mon,day,hour,min
