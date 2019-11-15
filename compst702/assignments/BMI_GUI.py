# convert_gui.py
# Program to convert Celsius to Fahrenheit using a simple
#   graphical interface.
"""Write a program that calculates BMI through a graphical user interface.
User should be able to fill in height, with feet and inches separately in two entry boxes,
and weight in pounds. It should display a button "Calculate". Only when the user clicks
anywhere inside this button (ignoring all other clicks), the program should calculate
and show BMI and the category (underweight/normal/overweight/obese). The category should
be displayed in different colors (for example, normal in green, obese in red etc.). After
that the "Calculate" button should turn into a "Quit" button. The program should close
only when the user clicks anywhere inside this button.

BMI = 703*weight/(height)**2

where weight is in pounds and height is in inches.

BMI Categories:
Underweight: < 18.5
Normal weight: 18.5–24.9
Overweight:  25–29.9
Obesity: >= 30

Note: You may find it easier to begin with the convert_gui.py program and then slowly modifying it. I
t may also help to first draw the interface on paper along with the coordinates."""


from graphics import *


def bmi_category(bmi):
    if bmi < 18.5:
        color = "yellow"
        category = "Underweight"
        return category, color
    elif 18.5 < bmi < 25.9:
        color = "green"
        category = "Normal weight"
        return category, color
    elif 25 < bmi < 29.9:
        color = "orange"
        category = "Overweight"
        return category, color
    else:
        color = "red"
        category = "Obese"
        return category, color


def main():
    win = GraphWin("BMI Calulator", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1, 3.5), "Height (ft):").draw(win)
    heightFtInput = Entry(Point(2.1, 3.5), 5)

    Text(Point(1, 3), "Height (in):").draw(win)
    heightInInput = Entry(Point(2.1, 3), 5)

    Text(Point(1, 2.5), "Weight (pounds):").draw(win)
    weightInput = Entry(Point(2.1, 2.5), 5)

    Text(Point(1, 1), "BMI:").draw(win)

    heightFtInput.draw(win)
    heightInInput.draw(win)
    weightInput.draw(win)

    output = Text(Point(2.1, 1), "")
    output.draw(win)
    button = Text(Point(1.5, 1.75), "Calculate")
    button.draw(win)
    rec = Rectangle(Point(1, 1.5), Point(2, 2))
    rec.draw(win)

    # wait for a mouse click
    clickPointY = win.getMouse().getY()
    clickPointX = win.getMouse().getX()
    print("click!")
    print(clickPointY, clickPointX)

    # convert input
    height = int(heightFtInput.getText()) * 12 + int(heightInInput.getText())
    weight = int(weightInput.getText())
    bmi = 703 * weight / height ** 2

    result = bmi_category(bmi)[0]
    fontColor = bmi_category(bmi)[1]
    outString = str(bmi) + "\n" + result
    gui_quit = False
    print(gui_quit)
    if not gui_quit:
        if 1.5 <= clickPointY <= 2 and 1 <= clickPointX <= 2:
            print("click1")
            output.setText(str(outString))
            output.setOutline(fontColor)
            button.setText("Quit")
            gui_quit = True
            # clickPointX, clickPointY = 0, 0
        else:
            print("miss!")


    clickPointY = win.getMouse().getY()
    clickPointX = win.getMouse().getX()
    print("click!")
    print(clickPointY, clickPointX)
    if gui_quit:
        if 1.5 <= clickPointY <= 2 and 1 <= clickPointX <= 2:
            print("click2")
            win.getMouse()
            win.close()

main()
