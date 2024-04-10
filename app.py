import customtkinter as ctk
import threading
from audit_listeners import start_event_listener, stop_event_listener, boolean

width = 400
height = 200

#"green"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
app = ctk.CTk()

audit_thread = threading.Thread(target=start_event_listener)

def start_audit_thread():
    global audit_thread
    if audit_thread is None or not audit_thread.is_alive():
        # Start start_event_listener only if it's not already running
        audit_thread = threading.Thread(target=start_event_listener)
        audit_thread.start()
    else:
        print("Event_listener is already running.")

    
def stop_audit():
    
    #audit_thread.join()
    boolean = False
    stop_event_listener()


app.geometry(f"{width}x{height}")
app.resizable(False, False)

ctk.set_appearance_mode("system")  # default
#ctk.set_appearance_mode("dark")
#ctk.set_appearance_mode("light")


app.title("Logon Sniffer")


start_btn = ctk.CTkButton(app, width=width/4, height=height/4, text="Start Audit", hover_color="darkgreen", text_color_disabled="darkblue", command=start_audit_thread)


stop_btn = ctk.CTkButton(app, width=width/4, height=height/4, text="Stop Audit", fg_color="red", hover_color="darkred",text_color_disabled="darkblue", command=stop_audit)



start_btn.pack()
stop_btn.pack()
#.........................................................................
app.mainloop()



