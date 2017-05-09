bursttime=[]
print("Enter number of process: ")
n=int(input())
processes=[]
for (i=0; i=n; i++)
 processes.insert(i,i+1)
print("Enter the burst time of the processes: ")
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
 int avgwaitingtime= avgwaitingtime+waitingtime[i]
 int avgturnaroundtime=avgturnaroundtime+turnaroundtime[i]
float avgwaitingtime=(avgwaitingtime)/n
float avgturnaroundtime=(avgturnaroundtime)/n
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for (i=0; i=n; i++)
 print((i)"\t" (bursttime[i]) "\t" (waitingtime[i]) "\t"  (turnaroundtime[i]))
print("Average Waiting time is:" (avgwaitingtime))
print("Average Turn Arount Time is:" (avgturnaroundtime))                   