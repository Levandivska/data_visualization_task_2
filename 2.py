#!/usr/bin/python

import datetime as dt
import matplotlib.pyplot as plt
import csv as csv
import numpy as np


print("Energy consumption")
Wk   =  ["понеділок", "вівторок", "середа", "четвер", "п’ятниця", "субота", "неділя"]
Week   =  {0:"понеділок", 1:"вівторок", 2:"середа", 3:"четвер", 4:"п’ятниця", 5:"субота", 6:"неділя"}   
MidDay=   [   0,             0,            0,          0,          0,            0,          0]
Monthes=  {0:'Січень', 1:'Лютий', 2:'Березень', 3:'Квітень', 4:'Травень', 5:'Червень', 6:'Липень', 
7:'Серпень', 8:'Вересень', 9:'Жовтень', 10:'Листопад', 11:'Грудень'}
Seasons = ["зима","весна","літо","осінь"]
Month=  ["Січень","Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", 
"Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]

reader = csv.reader(open("data.csv","r"),delimiter=';')
#      AES;TEC;VDE;TES;GES;GAES_GEN;CONSUMPTION;GAES_PUMP;UK_BLR_RUS;UK_EURO;UK_MLD;


Sources=['ГЕС', 'АЕС', 'ТЕЦ', 'ВДЕ', 'ТЕС', 'ГАЕС']

#        1 2 3 4 5 6 7 8 9 10 11 12   
MidMon= [0]*12
Years=  [2014,2015,2016,2017,2018,2019,2020]
Day=[0]*24
for t in range(24):
        Day[t]=t

#----------------------------------1-----------------------------------------
MidYearAES=             [0]*7
MidYearTEC=             [0]*7
MidYearVDE=             [0]*7
MidYearTES=             [0]*7
MidYearGES=             [0]*7
MidYearGAES_GEN=        [0]*7

        
#----------------------------------2-----------------------------------------
SumDayCONS  = [0]*366
SumHourCONS = [0]*24
#----------------------------------3-----------------------------------------
MidHourAES=             [0]*24
MidHourTEC=             [0]*24
MidHourVDE=             [0]*24
MidHourTES=             [0]*24
MidHourGES=             [0]*24
MidHourGAES_GEN=        [0]*24
MidHourCONS=            [0]*24
MidHourGAES_PUMP=       [0]*24
MidHourUK_BLR_RUS=      [0]*24
MidHourConsUK_EURO=     [0]*24
MidHourConsUK_MLD=      [0]*24


#-----------------------------------4----------------------------------
MidSeasonCONS=[ [0]*24 for i in range(4) ]
MidMontheCONS=[ [0]*24 for i in range(12) ]


errors=0;

def vseason(text):
        index = 0
        for day in Month:
                   index += 1
                   if text == day:
                        if 3 <= index <= 5:
                            return 'Весна'
                        elif 6 <= index <= 8:
                            return 'Лето'
                        elif 9 <= index <= 11:                           
                            return 'Осень'
                        else:
                            return 'Зима'
                            

def season(m):
        if (m<2):
                return 0
        if (m<5):
                return 1
        if (m<8):
                return 2
        if (m<11):
                return 3
        return 0

def to_int(str):
           try:
             return int(str)
           except ValueError:
                 global errors
                 errors+=1
                 return 0

counter=0
for row in reader:
        AES=to_int(row[1])
        TEC=to_int(row[2])
        VDE=to_int(row[3])
        TES=to_int(row[4])
        GES=to_int(row[5])
        GAES_GEN=to_int(row[6])
        CONS=to_int(row[7])#CONSUMPTION
        GAES_PUMP=to_int(row[8])
        UK_BLR_RUS=to_int(row[9])
        UK_EURO=to_int(row[10])
        UK_MLD=to_int(row[11])
        hh=to_int(row[0].split("-")[0]) #час суток
        dd=to_int(row[0].split("-")[1].split(".")[0])#день
        mm=to_int(row[0].split("-")[1].split(".")[1])#месяц 
        yy=to_int(row[0].split("-")[1].split(".")[2])#год
#-----------------------1----------------------        
        MidYearAES[yy-2015]+=AES
        MidYearTEC[yy-2015]+=TEC
        MidYearVDE[yy-2015]+=VDE
        MidYearTES[yy-2015]+=TES
        MidYearGES[yy-2015]+=GES
        MidYearGAES_GEN[yy-2015]+=GAES_GEN
#-----------------------2----------------------
        SumDayCONS[int(dt.date(yy, mm, dd).strftime('%j'))-1]+=CONS
        SumHourCONS[hh-1]+=CONS
#-----------------------3----------------------
        MidHourAES[hh-1]+=AES
        MidHourTEC[hh-1]+=TEC
        MidHourVDE[hh-1]+=VDE
        MidHourTES[hh-1]+=TES
        MidHourGES[hh-1]+=GES
        MidHourGAES_GEN[hh-1]+=GAES_GEN
#-----------------------4-----------------------
        MidSeasonCONS[season(mm-1)][hh-1]+=CONS
        MidMontheCONS[mm-1][hh-1]+=CONS
        
        
        counter+=1
        dof=dt.datetime(yy,mm,dd)
        MidDay[dof.weekday()]+=CONS
        
	
#for i in range(7):
#        MidYear[i]/=counter
#        MidDay[i]/=(counter*7)
        


#1.-Як змінювалась структура генерації електроенергії за роками?
#2.-Як залежить споживання електроенергії від дня року та години доби?
#3.-Як змінюється генерація електроенергії з різних джерел впродовж доби?
#4.-Як змінюється споживання електроенергії впродовж доби у розрізі місяців року та пір року?   


#print(MidYear)

print ("Errors %i" % errors)

#------------------------------------------------1------------------------------------	
#        MidYearAES AES
#        MidYearTEC TEC
#        MidYearVDE VDE
#        MidYearTES TES
#        MidYearGES GES
#        MidYearGAES_GEN GAES_GEN

fig, ax = plt.subplots()

Year=Years #range(7)

ax.bar(Year, MidYearAES, label="АЕС" )
ax.bar(Year, MidYearTEC, label="ТЕС" )
ax.bar(Year, MidYearVDE, label="ВЕС" )
ax.bar(Year, MidYearTES, label="ТЕЦ" )
ax.bar(Year, MidYearGES, label="ГЄС" )
ax.bar(Year, MidYearGAES_GEN, label="ГАЄС" )

ax.set_facecolor('seashell')

fig.set_figwidth(12)   
fig.set_figheight(6)    
fig.set_facecolor('floralwhite')
ax.set(xlabel='Рік',ylabel='Генерація, МВт')
ax.legend(loc=1)
plt.title('Cтруктура генерації електроенергії за роками.')
plt.show()

#------------------------------------------------2------------------------------------	

SumDayCONS[365]*=3.5 #компенсация высокосного



fig,ax = plt.subplots()
ax.plot(range(366),SumDayCONS)
ax.grid(axis='x',color='0.95')
ax.grid( axis='y',color='0.95')
plt.title('Залежність споживання електроенергії від дня року')
ax.set(xlabel='Номер дня',ylabel='Споживання, МВт')
plt.show()

fig,ax = plt.subplots()
ax.plot(range(24),SumHourCONS)
ax.grid(axis='x',color='0.95')
ax.grid( axis='y',color='0.95')
plt.title('Залежність споживання електроенергії від години доби')
ax.set(xlabel='Час доби',ylabel='Споживання, МВт')
plt.show()



#------------------------------------------------3------------------------------------	
for hh in range(24):
        MidHourAES[hh-1]/=counter
        MidHourTEC[hh-1]/=counter
        MidHourVDE[hh-1]/=counter
        MidHourTES[hh-1]/=counter
        MidHourGES[hh-1]/=counter
        MidHourGAES_GEN[hh-1]/=counter
        
fig,ax = plt.subplots()
ax.plot(Day,MidHourGES,label='ГЕС')
ax.plot(Day,MidHourAES,label='АЕС')
ax.plot(Day,MidHourTEC,label='ТЕЦ')
ax.plot(Day,MidHourVDE,label='ВДЕ')
ax.plot(Day,MidHourTES,label='ТЕС')
ax.plot(Day,MidHourGAES_GEN,label='ГАЕС')

ax.grid(axis='x',color='0.95')
ax.grid( axis='y',color='0.95')
ax.legend(title='Тип джерела:')
plt.title('Середньорічна генерація електроенергії з різних джерел впродовж доби')
ax.set(xlabel='Час доби',ylabel='Генерація, МВт')

plt.show()

#------------------------------------------------4--------------------------------------	

fig,ax = plt.subplots()
ax.grid(axis='x',color='0.95')
ax.grid( axis='y',color='0.95')

plt.title('Споживання електроенергії впродовж доби у розрізі місяців року')
ax.set(xlabel='Час доби',ylabel='Споживання, МВт')
ax.plot(Day,MidMontheCONS[0],label=Month[0])
ax.plot(Day,MidMontheCONS[1],label=Month[1])
ax.plot(Day,MidMontheCONS[2],label=Month[2])
ax.plot(Day,MidMontheCONS[3],label=Month[3])
ax.plot(Day,MidMontheCONS[4],label=Month[4])
ax.plot(Day,MidMontheCONS[5],label=Month[5])
ax.plot(Day,MidMontheCONS[6],label=Month[6])
ax.plot(Day,MidMontheCONS[7],label=Month[7])
ax.plot(Day,MidMontheCONS[8],label=Month[8])
ax.plot(Day,MidMontheCONS[9],label=Month[9])
ax.plot(Day,MidMontheCONS[9],label=Month[10])
ax.plot(Day,MidMontheCONS[9],label=Month[11])

ax.legend(title='Місяць',loc=1)
plt.show()

fig,ax = plt.subplots()
ax.grid(axis='x',color='0.95')
ax.grid( axis='y',color='0.95')

plt.title('Споживання електроенергії впродовж доби у розрізі пір року')
ax.set(xlabel='Час доби',ylabel='Споживання, МВт')
ax.plot(Day,MidSeasonCONS[0],label=Seasons[0])
ax.plot(Day,MidSeasonCONS[1],label=Seasons[1])
ax.plot(Day,MidSeasonCONS[2],label=Seasons[2])
ax.plot(Day,MidSeasonCONS[3],label=Seasons[3])


ax.legend(title='Пора року:',loc=1)
plt.show()




print ("thats all, folks")
	
	
	
	
