import wmi
from time import sleep
from datetime import datetime, timedelta

sleep_time = 10
batch_size = 100
minutes = 10  # Max time in minutes before event had occurred
event_id = 4675
logfile = "Security"
boolean = False

# Create a WMI object
connection = wmi.WMI()

# Define a function to fetch events within the recent time window
def fetch_recent_events():
    # Calculate the start time for the time window (recent 10 minutes)
    start_time = datetime.now() - timedelta(minutes=minutes)

    # Fetch events within the specified time window
    events = connection.Win32_NTLogEvent(Logfile=logfile)

    # Process each event
    print(len(events))
    if len(events) > 0:
        boolean = True
        for event in events:
            # Check if the event matches the event ID and falls within the time window
            if event.EventIdentifier == event_id and event.TimeGenerated >= start_time:
                # Print event information
                print("Event Type:", event.EventType)
                print("Event Code:", event.EventCode)
                print("Event Message:", event.Message)
                print("Event Time:", event.TimeGenerated)
                print("----------------------------------------")

                # Check if the event represents a success or a failure
                if event.EventType == "SuccessAudit":  # Check EventType for success
                    print("Event Type: Success")
                elif event.EventType == "FailureAudit":  # Check EventType for failure
                    print("Event Type: Failure")
                else:
                    print("Event Type: Unknown")  # Unknown event type
    
    else:
        boolean = False

if __name__=="__main__"
    # Continuously fetch and process events
    print("Events:........................................................................")
    print()
    print()

    index = 0
    while 1:
        if boolean:
            print(f"Batch No: {index}\n")
            fetch_recent_events()
            
            index += 1
        sleep(sleep_time)

