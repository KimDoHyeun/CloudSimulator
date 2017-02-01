import csv
import os

def workload_generator(path):

    workloadlist=[]
    VM_Workloadlist=[]
    filenames=os.listdir(path)
    for filename in filenames: 

	path1,ext=os.path.splitext(path+filename)
	print(path+filename)
	if ext=='.csv' :
	    print(path1)
	    workloadlist.append(path+filename)
	    print (path1)
    for workload in workloadlist:
	
	with open(workload) as csvfile:
	
	   vm_id,work=read_workload(csvfile)
	   VM_Workloadlist.append((vm_id,work))
    return VM_Workloadlist	

def read_workload(csvfile):
   
    reader=csv.reader(csvfile,delimiter=',')
    
    first_line=next(reader)
    vm_id=first_line[0]
    time=first_line[1]
    for row in reader:
	print (row[0],row[1]) 
    return vm_id,time
workload_generator("workload/")
	    
