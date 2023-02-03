import turtle
import pandas

image = "Blank_Periodic_Table.png"

screen = turtle.Screen()
turtle.bgpic(image)
screen.title("Periodic Table Quiz")

# def get_mouse_click(x, y):
#     """Gets the mouse coordinates for each element in the table"""
#     print(x, y)


# turtle.onscreenclick(get_mouse_click)

# config variables
correct_el = []
score = 0
is_playing = True

data = pandas.read_csv("periodic_table_quiz.csv")

elements_count = len(data.Element.to_list())

while is_playing:
    user_answer = screen.textinput(title="Guess the elements",
                                   prompt=f"Type an element ({score}/{elements_count}):").capitalize()

    element = data[data.Element == user_answer]

    if user_answer == "Exit":
        break
    elif element.empty or user_answer in correct_el:
        pass
    else:
        correct_el.append(user_answer)

        # writing the element on the table
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(element.x), int(element.y))
        t.write(user_answer)

        score += 1
        if score == elements_count:
            is_playing = False


turtle.mainloop()
