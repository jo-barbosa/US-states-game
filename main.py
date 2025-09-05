import pandas as pd

# data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#
# colors = data['Primary Fur Color'].value_counts()
# colors_df = pd.DataFrame(colors)
# print(colors_df)
# colors_df.to_csv('squirrel_count.csv')

# US States Game
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

correct_guesses = 0
data = pd.read_csv('50_states.csv')
states = data['state'].to_list()

while correct_guesses < 50:
    # answer = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    answer = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state's name?").title()
    if answer in states:
        correct_guesses += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


turtle.mainloop()
