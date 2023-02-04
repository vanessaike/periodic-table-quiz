import turtle
import pandas

image = "Blank_Periodic_Table.png"

screen = turtle.Screen()
turtle.bgpic(image)
screen.title("Periodic Table Quiz")

t = turtle.Turtle()
t.hideturtle()
t.penup()

# def get_mouse_click(x, y):
#     """Gets the mouse coordinates for each element in the table"""
#     print(x, y)


# turtle.onscreenclick(get_mouse_click)

correct_el = []
score = 0
is_playing = True

data = pandas.read_csv("periodic_table_quiz.csv")

elements = data.Element.to_list()

while is_playing:
    user_answer = screen.textinput(title="Guess the elements",
                                   prompt=f"Type an element ({score}/{len(elements)}):").capitalize()

    element = data[data.Element == user_answer]

    if user_answer == "Exit":
        # write all the elements that were not guessed
        elements_to_learn = [i for i in elements if i not in correct_el]

        for el in elements_to_learn:
            curr_el = data[data.Element == el]
            t.goto(int(curr_el.x), int(curr_el.y))
            t.pencolor("red")
            t.write(curr_el.Element.values[0])

        break
    elif element.empty or user_answer in correct_el:
        pass
    else:
        correct_el.append(user_answer)

        # writing the element on the table
        t.goto(int(element.x), int(element.y))
        t.write(user_answer)

        score += 1
        if score == len(elements):
            is_playing = False


turtle.mainloop()
