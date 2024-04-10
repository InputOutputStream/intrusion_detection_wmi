import wmi
#import audit
import threading
from time import sleep

boolean = False

def start_event_listener():
    print("Audit Started")
    
    i = 0
    while boolean is not True:
        print(f"Passage {i}")
                   
        i+=1
        sleep(3)
    
    return



def stop_event_listener():
    
    global boolean

    if boolean is not False:
        print("Event Listener is Not Runing")
    
    else:
        boolean = True
        print("Audit Stopped")

    return

