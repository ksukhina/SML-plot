#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:56:19 2023

@author: katrusia
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#change when needed
MINUTES_PER_DAY = 1440

startDay = 341      # Day to start collecting data
startHour = 19   # Hour of the day to start collecting data
startMinute = 16   # Minute of the day to start collecting data
dMinutes = 191   # Amount of minutes to record

# turns start hour and start minute into total start time in minutes
sTime = 0
if startHour != 0:
    sTime = (startHour * 60) + startMinute
else: 
    sTime = startMinute
    

#SML data read in
year = '2002'
smlfile = ('/Users/katrusia/Desktop/Internship 2022-2023/'+year+'_supermag.txt')

f1 = open(smlfile,'r')

n = -1
delim = "2002"

years = []
months = []
days = []
hours = []
minutes = []
dayOfYear = []

sml = []

n = 0
for line in f1:
    line = line.strip()
    
    #Skip to the data
    if delim not in line:
        continue
    
    columns = line.split()
    
    # Collect the data from the file
    years.append(columns[0])
    months.append(columns[1])
    days.append(columns[2])
    hours.append(columns[3])
    minutes.append(columns[4])
    sml.append(columns[7])
    
    # Records the minute and day of the year for each minute of data
    dayOfYear.append(int(n / MINUTES_PER_DAY) + 1)
    n += 1

f1.close()

year_arr = np.array(years, dtype = int)
month_arr = np.array(months, dtype = int)
day_arr = np.array(days, dtype = int)
hour_arr = np.array(hours, dtype = int)
min_arr = np.array(minutes, dtype = int)

sml_arr = np.array(sml, dtype = int)


#AL data read in
omnifile = ('/Users/katrusia/Desktop/Internship 2022-2023/omni_min2002.asc')


f = open(omnifile,'r')

n = -1

years = []
days = []
hours = []
minutes = []
dayOfYear = []
ae = []
al = []
au = []


for line in f:
    line = line.strip()
    columns = line.split()
   
    years.append(columns[0])
    days.append(columns[1])
    hours.append(columns[2])
    minutes.append(columns[3])
    
    
    ae.append(columns[37])
    al.append(columns[38])
    au.append(columns[39])
  
    # Records the minute and day of the year for each minute of data
    dayOfYear.append(int(n / MINUTES_PER_DAY) + 1)

    n += 1

       
f.close()

#doy = np.array(days, dtype = int)
hour_arr = np.array(hours, dtype = int)
minutes = np.array(minutes, dtype = int)

ae = np.array(ae, dtype = int)
al = np.array(al, dtype = int)
au = np.array(au, dtype = int)


# #SMC mw seasonal read in
# supermagfile='/Users/katrusia/Desktop/Internship 2022-2023/SMCs_Supermag_'+year+'_mw_seasonal.txt'

# f2 = open(supermagfile, 'r')

# #SMC data 
# DOY = []
# startTime = []
# endTime = []
# duration = []

# for line in f2:
#     line = line.strip()
#     columns = line.split()
    
#     DOY.append(columns[1])
#     startTime.append(columns[2])
#     endTime.append(columns[3])
#     duration.append(columns[4])
    
# f2.close()


#AL and SML plotting 
t1 = (dayOfYear[(startDay - 1) * MINUTES_PER_DAY] - 1)  # Starting day
t1 = t1 * MINUTES_PER_DAY + sTime   # Convert the starting day to minute
t2 = t1 + dMinutes


domain = np.linspace((t1/60)%24, (t2/60)%24, t2 - t1)
sml_range = sml_arr[t1 : t2]

al_range = al[t1 : t2]

#SMC plotting
smc_sml_plot = sml_arr[t1 : t2]

fig = plt.figure()

plt.xlabel('Hours')
plt.ylabel('AL (nT), SML(nT), SML_SMC')
plt.grid()
plt.plot(domain, al_range, 'r')
plt.plot(domain, sml_range, 'g')
plt.plot(domain, smc_sml_plot, 'b')

# to add a date to the title but needs to be automated
date = str(datetime.strptime('2002-12-07 19:16', '%Y-%m-%d %H:%M'))
plt.title('SML SMC for ' + date)
