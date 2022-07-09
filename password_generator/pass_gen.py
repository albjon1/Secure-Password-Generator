import tkinter as tk
import random
import ctypes as ct
import os

# Window
window = tk.Tk()
window.title("Secure Password Generator V1.0")
window.geometry('570x300')
window.configure(bg='grey12')
window.iconphoto(False, tk.PhotoImage(file='icon.png'))
window.resizable(width=False, height=False)

chars_str = '''52E*M1mO*x#l6C*3GUTi@DwAJ*9g1H#34@7*YbN53yX*j0k_8
zqh_os5v3a_RFWZ_fXH54ewD9_*YsBKcEMyTFPjNCoU0*@9hmGrtO3qn3_ixL4@*2gI'''
generated_pass_list = []


def generate_pass():
    global final_pass
    pass_input_len = int(input_box.get())
    if pass_input_len >= 10 and pass_input_len <= 40:
        for i in range(pass_input_len):
            list_choice = random.choice(chars_str)
            generated_pass_list.append(list_choice)
            random.shuffle(generated_pass_list)
        final_pass = ''.join(generated_pass_list)
        pass_lbl.config(text=f'Password: {final_pass}')
    elif pass_input_len > 40:
        ct.windll.user32.MessageBoxW(
         0, 'Maximum password length is 40', 'Error Raised', 0)
    elif pass_input_len < 10:
        ct.windll.user32.MessageBoxW(
         0, 'Password length must be 10 or more', 'Error Raised', 0)


def clipboard():
    global copy_label
    if len(generated_pass_list) == 0:
        ct.windll.user32.MessageBoxW(
         0, 'Password has not been generated yet', 'Error Raised', 0)
    else:
        text = final_pass
        clip_command = 'echo ' + text + '| clip'
        os.system(clip_command)
        copy_label = tk.Label(
         window,
         text='Copied to clipboard!',
         font='consolas',
         bg='grey12',
         fg='green')
        copy_label.pack(pady=21)


def clear_password():
    generated_pass_list.clear()
    pass_lbl.config(text=generated_pass_list)
    copy_label.destroy()


def save():
    if len(generated_pass_list) == 0:
        ct.windll.user32.MessageBoxW(
         0, 'Password has not been generated yet', 'Error Raised', 0)
    else:
        with open('password.txt', 'w') as pswd_file:
            pswd_file.write(f'Password -> {final_pass}')
        ct.windll.user32.MessageBoxW(
         0, 'Successfully saved password', 'Success', 0)


def light():
    window.configure(bg='white')
    title_lbl.config(bg='white', fg='black')
    input_box.config(bg='white', fg='black')
    dark_theme_button.config(bg='white', fg='black')
    light_theme_button.config(bg='white', fg='black')
    generate_button.config(bg='white', fg='black')
    clear_button.config(bg='white', fg='black')
    pass_lbl.config(bg='white', fg='black')
    clipboard_button.config(bg='white', fg='black')
    save_button.config(bg='white', fg='black')
    copy_label.config(bg='white')


def dark():
    window.configure(bg='grey12')
    title_lbl.config(bg='grey12', fg='#C8C8C8')
    input_box.config(bg='grey12', fg='#C8C8C8')
    dark_theme_button.config(bg='grey12', fg='#C8C8C8')
    light_theme_button.config(bg='grey12', fg='#C8C8C8')
    generate_button.config(bg='grey12', fg='#C8C8C8')
    clear_button.config(bg='grey12', fg='#C8C8C8')
    pass_lbl.config(bg='grey12', fg='#C8C8C8')
    clipboard_button.config(bg='grey12', fg='#C8C8C8')
    save_button.config(bg='grey12', fg='#C8C8C8')
    copy_label.config(bg='grey12')


print('built by albjon V1.0')
# Enter Password Length Label
title_lbl = tk.Label(
 window,
 bg='grey12',
 fg='#C8C8C8',
 text='Enter Password Length',
 font='consolas')
title_lbl.pack()

# Password Length Entry Widget
input_box = tk.Entry(
 window,
 bg='grey12',
 fg='#C8C8C8',
 selectbackground='#C8C8C8',
 insertbackground='#C8C8C8')
input_box.pack(pady=20)

# Theme Buttons
light_theme_button = tk.Button(
 window,
 text=' 🌕 ',
 command=light,
 bg='grey12',
 fg='#C8C8C8')
light_theme_button.place(x=77, y=1)

dark_theme_button = tk.Button(
 window,
 text=' 🌑 ',
 command=dark,
 bg='grey12',
 fg='#C8C8C8')
dark_theme_button.place(x=106, y=1)

# Generate Button
generate_button = tk.Button(
 window,
 text='Generate',
 command=generate_pass,
 bg='grey12',
 fg='#C8C8C8')
generate_button.pack(pady=5)

# Clear Button
clear_button = tk.Button(
 window,
 text='Clear',
 command=clear_password,
 bg='grey12',
 fg='#C8C8C8')
clear_button.pack(pady=5)

clipboard_button = tk.Button(
 window,
 text='Copy',
 command=clipboard,
 bg='grey12',
 fg='#C8C8C8')
clipboard_button.place(x=38, y=1)

save_button = tk.Button(
 window,
 text='Save ',
 command=save,
 bg='grey12',
 fg='#C8C8C8')
save_button.place(x=0, y=1)

# Generated Password Label
pass_lbl = tk.Label(
 window,
 bg='grey12',
 fg='#C8C8C8',
 text=generated_pass_list,
 font='consolas')
pass_lbl.pack(pady=5)

window.mainloop()
