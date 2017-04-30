total = 0
priority=[]
processes={}
bt=[]      #burst time
at=[]		#arrival time
n = input("Enter number of processes:")
for i in range (0,n):
	priority_no=input("Priority number is:")
	priority.append(priority_no)
	a_time=input("Arrival Time is:")
	at.append(a_time)
	b_time=input("Burst Time is:")
	bt.append(b_time)
	processes[priority[i]] = [i+1 , at[i] , bt[i]]

print "Priority#	Arrival Time           Burst Time"
for i in range (0,n):
	print priority[i] , "\t\t\t" , at[i], "\t\t\t" , bt[i] 

priority.sort()

total = processes.get(priority[0])[1]
min = total
if(total>0):
	print '0 -------' , total 

for i in range (0,n):
	total = total + processes.get(priority[i])[2]
	print min , "________" , total
	min = total