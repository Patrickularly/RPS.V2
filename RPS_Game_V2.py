import random
import customtkinter as ct

def center_window(root, width, height):
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f'{width}x{height}+{x}+{y}')

def score_update():
    p_count.configure(text=f'0{player_wins}')
    c_count.configure(text=f'0{bot_wins}')

def winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return f'Draw! Both chose {bot_choice}', 0, 0
    wins = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}
    if wins[player_choice] == bot_choice:
        return f'{player_choice} beats {bot_choice}. You win!', 1, 0
    else:
        return f'{bot_choice} beats {player_choice}. You lose!', 0, 1
    
def on_button_click(button_id):
    global player_wins, bot_wins
    player_choice = options[button_id]
    bot_choice = random.choice(options)
    result_text, player_score, bot_score = winner(player_choice, bot_choice)
    player_wins += player_score
    bot_wins += bot_score
    score_update()
    gameplay_label.configure(text=result_text)

def reset_button():
    global player_wins, bot_wins
    player_wins = 0
    bot_wins = 0
    score_update()
    gameplay_label.configure(text='Chose your weapon!')

if __name__ == "__main__":
    root = ct.CTk()
    root.title('ROCK - PAPER - SCISSORS')
    center_window(root, 440,430)
    root.resizable(False, False)
    root.grid_columnconfigure((0), weight=1)

    player_wins = 0
    bot_wins = 0
    options= ['Rock', 'Paper', 'Scissors']

    background = ct.CTkFrame(root, border_color='#5fab9c', border_width=3, fg_color='#051e1a')
    background.grid(row=0, column=0, padx=2, pady=5)

    # SCORES FRAME
    base_frame = ct.CTkFrame(master=background, fg_color='#29f3cc')
    base_frame.grid(row=1,column=0, pady=(20,10), padx=(20), sticky='nesw', columnspan=2)
    base_frame.grid_columnconfigure((0,1),weight=1)

    player_frame = ct.CTkFrame(master=base_frame, fg_color='transparent')
    player_frame.grid(row=0,column=0, pady=(10), padx=(20,10), sticky='ew')

    cpu_frame = ct.CTkFrame(master=base_frame, fg_color='transparent')
    cpu_frame.grid(row=0,column=1, pady=(10), padx=(10,20), sticky='ew')

    p_label = ct.CTkLabel(master=player_frame, font=('Arial',20,'bold'), text='PLAYER', text_color='black')
    p_label.grid(row=0, column=0, pady=(5), padx=(10,15))

    c_label = ct.CTkLabel(master=cpu_frame, font=('Arial',20,'bold'), text='CPU       ', text_color='black')
    c_label.grid(row=0, column=1, pady=(5), padx=(15,10))

    pc_frame = ct.CTkFrame(master=player_frame, fg_color='white', border_color='black', border_width=2)
    pc_frame.grid(row=0, column=1, pady=(5), padx=(0,5))

    cc_frame = ct.CTkFrame(master=cpu_frame, fg_color='white', border_color='black', border_width=2)
    cc_frame.grid(row=0, column=0, pady=(5), padx=(5,0))

    p_count = ct.CTkLabel(master=pc_frame, font=('Arial',20,'bold'), text='00',  text_color='black')
    p_count.grid(row=0, column=0, padx=(10), pady=2, sticky='ew')

    c_count = ct.CTkLabel(master=cc_frame, font=('Arial',20,'bold'), text='00', text_color='black')
    c_count.grid(row=0, column=0, padx=(10), pady=2)

    gameplay_label = ct.CTkLabel(master=background, fg_color='transparent', anchor='center', text='Chose your weapon!',text_color='#29f3cc',font=('Arial', 20, 'bold'))
    gameplay_label.grid(row=2, column=0, columnspan=2, sticky='nsew', pady=(5,40), padx=(20))

    # - - - BUTTONS - - - 
    leave = ct.CTkButton(background, text='Quit', text_color='#051e1a', font=('Arial',13,'bold'), hover_color='#f3cc29',fg_color='#29f3cc', command=root.quit)
    leave.grid(row=6, column= 0, padx=(20,10), pady=(40,20), sticky="ew", columnspan=1)

    reset = ct.CTkButton(background, text='Reset',text_color='#051e1a',font=('Arial',13,'bold'), hover_color='#f3cc29',fg_color='#29f3cc', command= lambda: reset_button())
    reset.grid(row=6, column= 1, padx=(10,20), pady=(40,20), sticky="ew", columnspan=1)

    # - - - WEAPONS - - -
    opt_frame = ct.CTkFrame(background, fg_color='transparent')
    opt_frame.grid(row=3, column=0, sticky='ew', columnspan=2, padx=(120))
    opt_frame.grid_columnconfigure((0), weight=1)

    for i, option in enumerate(options):
            button = ct.CTkButton(opt_frame, font=('Arial', 20, 'bold'), corner_radius=20, text=option, text_color='#f3cc29', fg_color='transparent', hover_color='#758e89', border_color='#29f3cc', border_width=2, command=lambda i=i: on_button_click(i))
            button.grid(row=i, column=0, padx=0, pady=(0, 20) if i < 2 else 0, ipady=5, sticky='ew', columnspan=2)

    root.mainloop()