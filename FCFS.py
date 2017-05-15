#!/usr/bin/env python

bursttime=[]          
print("Enter number of process: ")
noOfProcesses=int(input())
print("Enter the burst time of the processes: \n")
bursttime=list(map(int, raw_input().split()))
waitingtime=[]       
avgwaitingtime=0   
turnaroundtime=[]	
avgturnaroundtime=0     
waitingtime.insert(0,0)
turnaroundtime.insert(0,bursttime[0])
for i in range(1,len(bursttime)):
	waitingtime.insert(i,waitingtime[i-1]+bursttime[i-1])
	turnaroundtime.insert(i,waitingtime[i]+bursttime[i])
	avgwaitingtime=avgwaitingtime+waitingtime[i]
	avgturnaroundtime=avgturnaroundtime+turnaroundtime[i]
	avgwaitingtime=float(avgwaitingtime)/noOfProcesses
	avgturnaroundtime=float(avgturnaroundtime)/noOfProcesses
	print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,noOfProcesses):
	print(str(i)+"\t\t"+str(bursttime[i])+"\t\t"+str(waitingtime[i])+"\t\t"+str(turnaroundtime[i]))
	print("\n")
	print("Average Waiting time is: "+str(avgwaitingtime))
	print("Average Turn Arount Time is: "+str(avgturnaroundtime))