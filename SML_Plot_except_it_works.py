#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:12:44 2023

@author: katrusia
"""

import numpy as np
import matplotlib.pyplot as plt

MINUTES_PER_DAY = 1440

delimYear = '2002'
smlFile = "/Users/katrusia/Desktop/Internship 2022-2023/" + delimYear + "_supermag.txt"


file = open(smlFile)

years = []
months = []
days = []
hours = []
minutes = []
smlData = []
dayOfYear = []

startDay = 140      # Day to start collecting data
startMinute = 0   # Minute of the day to start collecting data
dMinutes = 1440     # Amount of minutes to record

n = 0
for line in file:
    line = line.strip()
    
    #Skip to the data
    if delimYear not in line:
        continue
    
    columns = line.split()
    
    # Collect the data from the file
    years.append(columns[0])
    months.append(columns[1])
    days.append(columns[2])
    hours.append(columns[3])
    minutes.append(columns[4])
    smlData.append(columns[7])
    
    # Records the minute and day of the year for each minute of data
    dayOfYear.append(int(n / MINUTES_PER_DAY) + 1)
    n += 1

file.close()

# Generates numpy arrays with the data
year_arr = np.array(years, dtype = int)
month_arr = np.array(months, dtype = int)
day_arr = np.array(days, dtype = int)
hour_arr = np.array(hours, dtype = int)
minutes_arr = np.array(minutes, dtype = int)
smlData_arr = np.array(smlData, dtype = float)

# Preventing potential errors
if startDay < 1: startDay = 1
if startDay > 365: startDay = 365

# Calculating the start and end times to plot
t1 = (dayOfYear[(startDay - 1) * MINUTES_PER_DAY] - 1)  # Starting day
t1 = t1 * MINUTES_PER_DAY + startMinute   # Convert the starting day to minute
t2 = t1 + dMinutes

# Preventing potential errors
if t1 >= len(smlData_arr): t1 = len(smlData_arr) - 1
if t2 > len(smlData_arr): t2 = len(smlData_arr)

# Domain and range values for plot
smlDomain = range(t1, t2)
smlRange = smlData_arr[t1 : t2]

# Plot
fig = plt.figure()
plt.title("Start Day of Year: " + str(startDay))
plt.xlabel("Time Elapsed (Minutes)")
plt.ylabel("SML (nT)")
plt.xlim([t1, t2])
plt.grid()
plt.plot(smlDomain, smlRange, 'm')
