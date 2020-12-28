import srccode as s
import time
import threading
from threading import *

t1=Thread(target=s.create,args=("venkat",21))
t1.start()
time.sleep(3)
#creation of a new key-value pair in the datastore

t2=Thread(target=s.create,args=("vignesh",22))
t2.start()
time.sleep(3)
#creation of another key-value pair in the data store

t3=Thread(target=s.read1,args=("venkat",))
t3.start()
print(s.read1("venkat"))
time.sleep(3)
#reads the value of the key and returns the result in the json format

t4=Thread(target=s.delete1,args=("venkat",))
t4.start()
time.sleep(3)
#deletes the key-value pair
