from tkinter import *
import pandas
from random import *


BACKGROUND_COLOR = "#B1DDC6"

# with open("./data/french_words.csv") as data_file:
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

word_dict = data.to_dict(orient="records")
count = 3
game_is_on = True
current_card = {}


def next_right():
    global current_card
    global word_dict
    word_dict.remove(current_card)
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_wrong()


def next_wrong():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_dict)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# print(english_word)
# print(french_word)

# TODO 1: create image with title, word, and button
window = Tk()
window.title("French Flash Cards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_wrong)
cross_button.grid(column=1, row=2)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=next_right)
check_button.grid(column=2, row=2)

front_image = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

back_image = PhotoImage(file="./images/card_back.png")


next_wrong()

# TODO 2: create second for other language

# TODO 3:


window.mainloop()
