#  This code work only for MacOS

import subprocess
import webbrowser
import pyautogui as pg
import time



def set_max_volume_mac():
    try:
        # Используем AppleScript для установки максимального уровня громкости
        applescript = '''
        set volume output volume 100
        '''
        subprocess.run(['osascript', '-e', applescript])
        print("Уровень громкости установлен на максимум.")
    except Exception as e:
        print("Произошла ошибка при установке уровня громкости:", e)

# URL веб-сайта, который вы хотите открыть
website_url = 'http://omfgdogs.com'

# Открываем веб-сайт в браузере по умолчанию
webbrowser.open(website_url)

# Устанавливаем максимальный уровень громкости на macOS
set_max_volume_mac()

time.sleep(1)
pg.click(678, 315)

