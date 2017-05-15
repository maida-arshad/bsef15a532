#!/usr/bin/env python

total = 0
priority=[]
processes={}
bursttime=[]
arrivaltime=[]	
noOfProcesses = input("Enter number of processes:")
for i in range (0,noOfProcesses):
	priority_no=input("The Priority number is:")
	priority.append(priority_no)
	arrival_time=input("The Arrival Time is:")
	arrivaltime.append(arrival_time)
	burst_time=input("The Burst Time is:")
	bursttime.append(burst_time)
	processes[priority[i]] = [i+1 , arrivaltime[i] , bursttime[i]]

print "   Priority_No	            Arrival Time           Burst Time"
for i in range (0,noOfProcesses):
	print priority[i] , "\t\t\t" , arrivaltime[i], "\t\t\t" , bursttime[i] 

priority.sort()

total = processes.get(priority[0])[1]
min = total
if(total>0):
	print '0 -------' , total 

for i in range (0,noOfProcesses):
	total = total + processes.get(priority[i])[2]
	print min , "______" , total
	min = total

