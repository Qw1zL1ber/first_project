import tkinter as tk
from pygame import mixer
import random 
from tkinter import messagebox

mixer.init()

score = 0
succes = ""
sound_guns = {
    'm4a1-s':'m4a1-s.wav','m41a':'m4a1.wav','negev':'negev.wav','awp':'awp.wav','glock':'glock.wav','ct_pletka':'ct_pletka.wav','t_pletka':'t_pletka.wav','mp7':'mp7.wav','revouler':'revouler.wav','mac10':'mac10.wav','scout':'scout.wav','usp':'usp.wav','xm':'xm.wav','обрез':'обрез.wav','p90':'p90.wav','p250':'p250.wav','mac7':'mac7.wav','ak47':'ak47.wav','galil':'galil.wav','cz':'cz.wav','deagle':'deagle.wav'
}

def succes_itog(chosen_weapon):
    global score
    if chosen_weapon == succes:
        messagebox.showinfo('SUCCES','Вы угадали!')
        score+=1
    else:
        messagebox.showinfo('WRONG','Вы не угадали')
    btn_label.config(text=f'Счет: {score}')
    if score == 21:
        messagebox.showinfo('Тест завершен', 'Вы угадали Всё! Perfect Job, вы на уровне PRO игрока!')
        score = 0
    next_round()

def play_current_sound():
    """Функция воспроизведения текущего загаданного звука"""
    if succes:
        sound_file = sound_guns[succes]
        try:
            mixer.music.load(sound_file)
            mixer.music.play()
        except Exception as e:
            print(f"Ошибка воспроизведения {sound_file}: {e}")

def next_round():
    """Функция подготовки нового раунда: выбирает оружие и перемешивает варианты ответов"""
    global succes
    
    all_weapons = list(sound_guns.keys())
    succes = random.choice(all_weapons)

    wrong_options = [w for w in all_weapons if w != succes]
    random_wrong = random.sample(wrong_options, 3)

    options = [succes] + random_wrong
    random.shuffle(options)

    for i in range(4):
        answer_buttons[i].config(text=options[i], command=lambda opt=options[i]:succes_itog(opt))

    play_current_sound()

root = tk.Tk()
root.geometry('500x500')
root['bg']="#0891D1"
root.title('Тест на звуки из кски')


btn_label = tk.Label(root,text=f'Ваш счет: 0',bg='#00D9FF')
btn_label.pack()

btn_sound = tk.Button(root,
                      bg="#00D9FF",
                      text='Послушать звук',
                      command=play_current_sound
                      )
btn_sound.pack(pady=20)
answer_buttons = []

for _ in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=20,bg="#00D9FF",height=2)
    btn.pack(pady=5)
    answer_buttons.append(btn)

next_round()
root.mainloop()