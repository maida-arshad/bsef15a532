priority=[]
processes={}
bursttime=[] 
arrivaltime=[]		
n = input("Enter number of processes:")
for (i=0; i=n; i++)
	priority_no=input("Priority number is:")
	a_time=input("Arrival Time is:")
	b_time=input("Burst Time is:")
	processes[priority[i]] = [i+1 , arrivaltime[i] , bursttime[i]]
print "Priority Number	Arrival Time           Burst Time"
for (i=0; i=n; i++)
	print (priority[i] , "\t" , arrivaltime[i], "\t" , bursttime[i])
