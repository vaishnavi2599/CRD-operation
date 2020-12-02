import threading
import time
import json
readpath="G:/"
from threading import *


def create(key,value,timeout=0,path=readpath):
    value=int(value)
    timeout=int(timeout)
    key=str(key)
    path=str(path)
    #print(key)
    d={}
    global readpath
    try:
        with open(path+"store.json",'r') as k:
            d=json.load(k)
            #print(d)
            #print(type(d))
            k.close()
    except:print("empty")

    if key in d:
        print("key already exists")
    elif(key.isalpha() and len(key)<=32):
        
        
        if int(len(d))<(1024*1024*1024) and int(value)<=(16*1024):
            if timeout==0:
                v=[{"value":value,"timeout":timeout,"path":path}]
            else:
                v=[{"value":value,"timeout":time.time()+timeout,"path":path}]
            d[key]=v
            f=open(path+"store.json","w")
            json.dump(d,f,indent=2)
            #print(type(d))
            #print(d)
            print("key created!")
            f.close()
        else:
            print("Memory limit exceeded!")
        #except:
         #   print("key must be a string")

    else:
        print("key should be a string!")
    
def read(key,path=readpath):
    global readpath
    key=str(key)
    
    path=str(path)
    
    readpath=path
    
    f=open(readpath+"store.json",'r')
    d=json.load(f)
    #print(d)    
    if key not in d:
        print("key does not exist! ")
    else:
        b=d[key]
        #print(b)
        if b[0]['timeout']!=0:
            if time.time()<b[0]['timeout']:
                print(json.dumps(b[0],indent=2))
            else:
                print("time-to-live of",key,"has expired")
                del d[key]
                f=open(readpath+"store.json","w")
                json.dump(d,f,indent=2)
                #print(d)
                
        else:
            print(json.dumps(b[0],indent=2))
            

def delete(key,path=readpath):
    key=str(key)
    global readpath
    
    #print(key,path)
    f=open(readpath+"store.json",'r')
    d=json.load(f)
    #print(d)
    if key not in d:
        print("key does not exist! ") 
    else:
        b=d[key]
        if b[0]['timeout']!=0:
            if time.time()<b[0]['timeout']: 
                del d[key]
                print("key deleted")
            else:
                del d[key]
                f=open(readpath+"store.json","w")
                json.dump(d,f,indent=2)
                #print(d)
                print("time-to-live of",key,"has expired!") #error message5
        else:
            del d[key]
            print("key is successfully deleted")
            f=open(readpath+"store.json","w")
            json.dump(d,f,indent=2)
            #print(d)
            f.close()


if __name__=="__main__":
    i=int(input("Enter 1 for CREATE, 2 for READ , 3 for DELETE, 0 for EXIT\n"))
    
    while i>-1:
        
        if i==1:
            j=input("Enter key,value,timeout(optional),path(optional)\n")
            k=tuple(j.split(","))
            #print(k)
            create(*k)
        elif i==2:
            j=input("Enter key,path(optional)\n")
            k=tuple(j.split(","))
            #print(k)
            read(*k)
        elif i==3:
            j=input("Enter key,path(optional)\n")
            k=tuple(j.split(','))
            
            delete(*k)
        elif i==0:
            break
        else:
            print("user entered a wrong value\n")
        i=int(input("Enter 1 for CREATE, 2 for READ , 3 for DELETE, 0 for EXIT\n"))

    
