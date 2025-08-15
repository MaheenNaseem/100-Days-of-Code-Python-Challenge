import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed = []

while len(guessed) < 50:
    if len(guessed) == 0:
        user_guess = screen.textinput("Guess the State", "Write a state name: ")
    else:
        user_guess = screen.textinput(f"{len(guessed)}/50 States Correct", "Write a state name: ")

    if not user_guess:  # Cancel button pressed
        break

    user_guess = user_guess.title()

    if user_guess == "Exit":  # Cancel button pressed
        # Day 25
        # missing_states = []
        # for state in states:
        #     if state not in guessed:
        #         missing_states.append(state)

        #Day 26 update - List Comprehension
        missing_states = [state for state in states if state not in guessed]
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to Learn")
        break

    if user_guess in guessed:
        user_guess = screen.textinput(f"{len(guessed)}/50 States Correct", "You've already guessed this. Guess Again: ")
        continue

    if user_guess in states:
        current_state = data[data.state == user_guess]
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(current_state.x.item(),current_state.y.item())
        turtle.write(user_guess, False, "center")
        guessed.append(user_guess)

turtle.mainloop()


