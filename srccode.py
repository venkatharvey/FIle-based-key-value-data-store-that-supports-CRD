import threading
from threading import *
import time

data={} #dictionary for storing our data

def create(key,value,timeout=0):
	if key in data:
		print("Error: Key already exists try different key") #error message if the key already exists in the datastore
	else:
		if (key.isalpha()): #returns true if the key is alphabet and process the if condition
			if len(data)<(1024*1020*1024) and value<=(16*102*1024): # The size of file storing data must be within 1GB and value must be within 16kb
				if timeout==0:
					l=[value,timeout]
				else:
					l=[value,time.time()+timeout]
			if len(key)<=32:
				data[key]=l
			else:
				print("Error:Memory limit exceeded") #error message if the len of the key exceeds 32chars 
		else:
			print("Error:Key name should be alphabet,no numbers or characters allowed") #error message if key other than alphabet is used
	
	
def read1(key):
	if key not in data: 
		print("Error:key does not exist") #error message if the key does not exist in the datastore
		
	else:
		t=data[key]
		if t[1]!=0: #checks timeout of the key =0
			if time.time()<t[1]: #checks the time to live of the key
				result=key+":"+str(t[0])
				return result #returns the value of the key in json format
			else:
				print("Error:Time-to-live for the key expired") #error message if the key is expired
		else:
			result=key+":"+str(t[0])
			return result #returns the value of the key in json format
			
def delete1(key):
	if key not in data:
		print("Error:key does not exist") #error message if the key does not exist in the datastore 
		
	else:
		t=data[key]
		if t[1]!=0: #checks timeout of the key=0
			if time.time()<t[1]:
				del data[key] #deletes the key
				print(key+" successfully deleted")
			else:
				print("Error:Time-to-live for the key expired") #error message if the key is expired
		else:
			del data[key] #deletes the key
			print(key+" successfully deleted") 

			
			#THANK YOU FRESH WORKS ......
