#Codificacion Climatica
import os,csv
#FUNCTIONS----------------------------------------------------

def GetYear(fact):
	year=fact[:4]
	year=int(year)
	year=year<<0b101111  #11111111111100000000000000000000000000000000000000000000000
	return year

def GetMonth(fact):
	month=fact[5:7]
	month=int(month)
	month=month<<0b101011
	return month

def GetDay(fact):
	day=fact[8:10]
	day=int(day)
	day=day<<0b100110
	return day

def GetHour(fact):
	hour=fact[11:13]
	hour=int(hour)
	hour=hour<<0b100001
	return hour

def GetMinute(fact):
	minute=fact[14:16]
	minute=int(minute)
	minute=minute<<0b11011
	return minute

def GetSec(fact):
	sec=fact[17:19]
	sec=int(sec)
	sec=sec<<0b10101
	return sec

def GetDes_Sec(fact):
	des_sec=fact[20:23]
	des_sec=int(des_sec)
	des_sec=des_sec<<0b1011
	return des_sec

def GetTZH(fact):
	time_zh=fact[24:26]
	time_zh=int(time_zh)
	time_zh=time_zh<<0b0110
	return time_zh

def GetTZM(fact):
	time_zm=fact[27:29]
	time_zm=int(time_zm)
	return time_zm
#--------------------------
def GetMinTemp(fact,counter):
	min_temp=data_file[counter][1]
	min_temp=int(min_temp)
	min_temp=min_temp<<0b1110
	return min_temp

def GetMaxTemp(fact,counter):
	max_temp=data_file[counter][2]
	max_temp=int(max_temp)
	max_temp=max_temp<<0b111
	return max_temp

def GetPrecipitation(fact,counter):
	precipitation=data_file[counter][3]
	precipitation=int(precipitation)
	return precipitation

#===============================================================================
directory=os.getcwd()
open_file=open(directory+'\\Date & Climate.csv')
read_file=csv.reader(open_file)
data_file=list(read_file)

open_to_write=open(directory+'\\Bit Data.csv','w')

counter=0

fact=data_file[1]
fact=str(''.join(fact))

for row in data_file:
	counter+=1

	if counter<int(read_file.line_num):

		fact=data_file[counter]
		fact=str(''.join(fact))

		year=GetYear(fact)
		#sfbits=sfbits^year


		month=GetMonth(fact)
		#sfbits=sfbits^month
		year=year^month


		day=GetDay(fact)
		#sfbits=sfbits^day
		year=year^day

		hour=GetHour(fact)
		#sfbits=sfbits^hour
		year=year^hour

		minute=GetMinute(fact)
		#sfbits=sfbits^minute
		year=year^minute

		sec=GetSec(fact)
		#sfbits=sfbits^sec
		year=year^sec

		des_sec=GetDes_Sec(fact)
		#sfbits=sfbits^des_sec
		year=year^des_sec

		time_zh=GetTZH(fact)
		#sfbits=sfbits^time_zh
		year=year^time_zh

		time_zm=GetTZM(fact)
		#sfbits=sfbits^time_zm
		year=year^time_zm
	#Temperatura-------------------------------------
		min_temp=GetMinTemp(fact,counter)
		#ttbits=ttbits^min_temp

		max_temp=GetMaxTemp(fact,counter)
		#ttbits=ttbits^max_temp
		min_temp=min_temp^max_temp

		precipitation=GetPrecipitation(fact,counter)
		#ttbits=ttbits^precipitation
		min_temp=min_temp^precipitation


		inputData=str(year)
		inputTemp=str(min_temp)
		inputTemp=(inputTemp+'\n')

		inputBits=[inputData,inputTemp]
		
		open_to_write.write(' , '.join(inputBits))