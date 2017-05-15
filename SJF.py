#!/usr/bin/env python

bursttime=[]     
print("Enter number of process: ")
noOfProcesses=int(input())
processes=[]
for i in range(0,noOfProcesses):
	processes.insert(i,i+1)
	print("Enter the burst time of the processes: \n")
	bursttime=list(map(int, raw_input().split()))
for i in range(0,len(bursttime)-1):  
	for j in range(0,len(bursttime)-i-1):
		if(bursttime[j]>bursttime[j+1]):
			temp=bursttime[j]
			bursttime[j]=bursttime[j+1]
			bursttime[j+1]=temp
			temp=processes[j]
			processes[j]=processes[j+1]
			processes[j+1]=temp
waitingtime=[]   
avgwaitingtime=0  
turnaroundtime=[]    
avgturnaroundtime=0   
waitingtime.insert(0,0)
turnaroundtime.insert(0,bursttime[0])
for i in range(1,len(bursttime)):  
	waitingtime.insert(i,waitingtime[i-1]+bursttime[i-1])
	turnaroundtime.insert(i,waitingtime[i]+bursttime[i])
	avgwaitingtime+=waitingtime[i]
	avgturnaroundtime+=turnaroundtime[i]
	avgwaitingtime=float(avgwaitingtime)/noOfProcesses
	avgturnaroundtime=float(avgturnaroundtime)/noOfProcesses
	print("\n")
	print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,noOfProcesses):
	print(str(i)+"\t\t"+str(bursttime[i])+"\t\t"+str(waitingtime[i])+"\t\t"+str(turnaroundtime[i]))
	print("\n")
	print("Average Waiting time is: "+str(avgwaitingtime))
	print("Average Turn Arount Time is: "+str(avgturnaroundtime))