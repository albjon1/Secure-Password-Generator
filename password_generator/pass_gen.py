import tkinter as tk
import random
import ctypes as ct

# Window
window = tk.Tk()
window.title("Secure Password Generator V1.0")
window.geometry('570x300')
window.configure(bg='grey12')
window.iconphoto(False, tk.PhotoImage(file='icon.png'))

random_chars = '''52EMmOx#l6C3GUTi@DwAJ9g1H#@7*YbNyX*j
0k8zqhosva_RFWZfPcdKerLS4up_IBnQtV'''
generated_pass_list = []


def generate_pass():
    pass_input_len = int(input_box.get())
    if pass_input_len >= 10 and pass_input_len <= 100:
        for i in range(pass_input_len):
            list_choice = random.choice(random_chars)
            generated_pass_list.append(list_choice)
        final_pass = ''.join(generated_pass_list)
        pass_lbl.config(text=f'Password: {final_pass}')
    elif pass_input_len > 100:
        ct.windll.user32.MessageBoxW(
         0, 'Maximum password length is 100', 'Error Raised', 0)
    elif pass_input_len < 10:
        ct.windll.user32.MessageBoxW(
         0, 'Password length must be 10 or more', 'Error Raised', 0)


def clear_password():
    generated_pass_list.clear()
    pass_lbl.config(text=generated_pass_list)


def creator(message):
    return message


print(creator('built by albjon V1.0'))

# Enter Password Length Label
title_lbl = tk.Label(window,
                     bg='grey12',
                     fg='#C8C8C8',
                     text='Enter Password Length',
                     font='consolas')
title_lbl.pack()


# Password Length Entry Widget
input_box = tk.Entry(window,
                     bg='grey12',
                     fg='#C8C8C8',
                     selectbackground='#C8C8C8',
                     insertbackground='#C8C8C8')
input_box.pack(pady=20)

# Generate Button
generate_button = tk.Button(window,
                            text="Generate",
                            command=generate_pass,
                            bg='grey12',
                            fg='#C8C8C8')
generate_button.pack(pady=5)

# Clear Button
clear_button = tk.Button(window,
                         text="Clear",
                         command=clear_password,
                         bg='grey12',
                         fg='#C8C8C8')
clear_button.pack(pady=5)

# Generated Password Label
pass_lbl = tk.Label(window,
                    bg='grey12',
                    fg='#C8C8C8',
                    text=generated_pass_list,
                    font='consolas')
pass_lbl.pack(pady=5)
window.mainloop()
