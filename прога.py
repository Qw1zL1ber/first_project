import subprocess
import tkinter as tk
from tkinter import messagebox

def is_process_running(process_name):
    try:
        cmd = f'tasklist /FI "IMAGENAME eq {process_name}"'
        output = subprocess.check_output(cmd, shell=True).decode('cp866', errors='ignore')
        return process_name.lower() in output.lower()
    except Exception:
        return False

def start_game(game_key):
    beautiful_name = games[game_key][0]
    launch_game = games[game_key][1]
    process_name = games[game_key][2] 
    
    if is_process_running(process_name):
        messagebox.showwarning("Внимание", f"Приложение {beautiful_name} уже запущено!")
        return
        
    try:
        subprocess.Popen(launch_game, shell=True)
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f"Игра {beautiful_name} успешно запущена через GUI!\n")
        messagebox.showinfo("Успех", f"Запускаю {beautiful_name}... Удачной игры!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось запустить: {e}")

games = {
    'cs2': ['Counter-Strike 2', 'start steam://rungameid/730', 'cs2.exe'],
    'субнатика': ['Subnautica 2', r"C:\Users\User\Desktop\Subnautica.2-InsaneRamZes\Subnautica2.exe", 'Subnautica2.exe'],
    'обои': ['Wallpaper Engine', r'C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\wallpaper64.exe', 'wallpaper64.exe'],
    'фейсит':['Faceit',r"C:\Users\User\Desktop\FACEIT.lnk",'FACEIT.exe'],
    'античит':['Faceit AntiCheat',r"C:\Users\Public\Desktop\FACEIT AC.lnk",'faceitclient.exe'],
    'геншин':['Genchin Impact',r"C:\Program Files\HoYoPlay\games\Genshin Impact game\GenshinImpact.exe",'GenshinImpact.exe']
}

root = tk.Tk()
root.configure(bg='red')
root['bg']="#A54C80"
root.title("Steam")
root.geometry("500x500")
color_button = "#680B0B"


label = tk.Label(root, 
                 text="Выберите игру для запуска:", 
                 font=("Impact", 14),
                 bg=root["bg"], 
                 fg='white',
                 pady=20)
label.pack() 

btn_cs = tk.Button( root,
                   text="Counter-Strike 2", 
                   font=("Courier New", 15),
                   bg=color_button, 
                   width=25, 
                   fg="white",
                    command=lambda: start_game('cs2'))
btn_cs.pack(pady=5)

btn_sub = tk.Button(root, 
                    text="Subnautica 2", 
                    font=("Courier New", 15), 
                    width=25, 
                    bg=color_button, 
                    fg="white",
                     command=lambda: start_game('субнатика'))
btn_sub.pack(pady=5)

btn_wall = tk.Button(root,
                    text="Wallpaper Engine",
                    font=("Courier New", 15),
                    width=25, 
                    bg=color_button,
                    fg="white",
                      command=lambda: start_game('обои'))
btn_wall.pack(pady=5)

btn_faceit = tk.Button(root,
                    text="Faceit",
                    font=("Courier New", 15),
                    width=25, 
                    bg=color_button,
                    fg="white",
                      command=lambda: start_game('фейсит'))
btn_faceit.pack(pady=5)

btn_anticheat = tk.Button(root,
                     text='Античит',
                     font=('Courier New',15),
                     width=25,
                     bg=color_button,
                     fg='white',
                     command=lambda: start_game('античит') )
btn_anticheat.pack(pady=5)

btn_genshin = tk.Button(root,
                     text='Genshin Impact',
                     font=('Courier New',15),
                     width=25,
                     bg=color_button,
                     fg='white',
                     command=lambda: start_game('геншин') )
btn_genshin.pack(pady=5)

btn_exit = tk.Button(root,
                     text='Выход',
                     font=('Courier New',12,'bold'),
                     width=15,
                     bg='white',
                     fg='black',
                     command = quit )
btn_exit.pack(pady=5)

root.mainloop()