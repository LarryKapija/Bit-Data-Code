import os,csv
#FUNCTIONS--------------------------------------
def GetYear(code):
	year=int(code)
	year=year>>0b101111
	return year

def GetMonth(code):
	month=int(code)
	month=month&0b11110000000000000000000000000000000000000000000
	month=month>>0b101011
	return month

def GetDay(code):
	day=int(code)
	day=day&0b1111100000000000000000000000000000000000000
	day=day>>0b100110
	return day

def GetHour(code):
	hour=int(code)
	hour=hour&0b11111000000000000000000000000000000000
	hour=hour>>0b100001
	return hour

def GetMinute(code):
	minute=int(code)
	minute=minute&0b111111000000000000000000000000000
	minute=minute>>0b11011
	return minute

def GetSec(code):
	sec=int(code)
	sec=sec&0b111111000000000000000000000
	sec=sec>>0b10101
	return sec

def GetDes_Sec(code):
	des_sec=int(code)
	des_sec=des_sec&0b111111111100000000000
	des_sec=des_sec>>0b1011
	return des_sec


def GetTZH(code):
	time_zh=int(code)
	time_zh=time_zh&0b11111000000
	time_zh=time_zh>>0b0110
	return time_zh

def GetTZM(code):
	time_zm=int(code)
	time_zm=time_zm&0b111111
	return time_zm
#------------------------------------------------
def GetMinTemp(data_file,counter):
	min_temp=int(data_file[counter][1])
	min_temp=min_temp&0b111111100000000000000
	min_temp=min_temp>>0b1110
	return min_temp

def GetMaxTemp(data_file,counter):
	max_temp=int(data_file[counter][1])
	max_temp=max_temp&0b11111110000000
	max_temp=max_temp>>0b111
	return max_temp

def GetPrecipitation(data_file,counter):
	precipitation=int(data_file[counter][1])
	precipitation=precipitation&0b1111111
	return precipitation


#==============================================================
directory=os.getcwd()
open_file=open(directory+'\\Bit Data.csv')
read_file=csv.reader(open_file)
data_file=list(read_file)


counter=0


for row in data_file:
	
	if counter<int(read_file.line_num):
		code=str(data_file[counter][0])
		
		year=GetYear(code)
		month=GetMonth(code)
		day=GetDay(code)
		hour=GetHour(code)
		minute=GetMinute(code)
		sec=GetSec(code)
		des_sec=GetDes_Sec(code)
		time_zh=GetTZH(code)
		time_zm=GetTZM(code)
		#--------------------
		min_temp=GetMinTemp(data_file,counter)
		max_temp=GetMaxTemp(data_file,counter)
		precipitation=GetPrecipitation(data_file,counter)

		DateAndTime=str(f'{year}-{month}-{day}T{hour}:{minute}:{sec}.{des_sec}-{time_zh}:{time_zm}')
		lista=[DateAndTime,str(min_temp),str(max_temp),str(precipitation)]
		print('\t'.join(lista))

		counter+=1
		#print(DateAndTime)
	
	





