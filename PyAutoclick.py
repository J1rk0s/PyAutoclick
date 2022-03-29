import keyboard
import win32api, win32con
import time
import tkinter as tk
    
root = tk.Tk()
root.geometry("500x500")
root.title("AUTOCLICKER")
root.config(bg='Blue')
def click():            
    while True:
        if keyboard.is_pressed('q'):                       
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            # key = "i"
            # keyboard.press(key)
            # keyboard.release(key)
            # time.sleep(0.01)           
        if keyboard.is_pressed('m'):
            break
frame = tk.Frame(root)
label = tk.Label(frame, text="Made by: J1rk0s", font='Arial')
start = tk.Button(frame, text="Click Me!", bg="Black", fg="White", command = click,width=10, height=2)
stauto = tk.Label(frame, text="To start press the button and then pres q and to stop the autoclicker pres m")
stauto.config(font=('Arial',10), pady=500)
label.pack()
frame.pack()
start.pack(side=tk.TOP, pady=50)
stauto.pack()
root.mainloop()
