from graphics import *


def bmi_category(bmi):
    if bmi < 18.5:
        color = "gold"
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
    heightFtInput.draw(win)

    Text(Point(1, 3), "Height (in):").draw(win)
    heightInInput = Entry(Point(2.1, 3), 5)
    heightInInput.draw(win)

    Text(Point(1, 2.5), "Weight (pounds):").draw(win)
    weightInput = Entry(Point(2.1, 2.5), 5)
    weightInput.draw(win)

    Text(Point(1, 1), "BMI:").draw(win)

    output = Text(Point(2.1, 1), "")
    output.draw(win)

    button = Text(Point(1.5, 1.75), "Calculate")
    button.draw(win)
    rec = Rectangle(Point(1, 1.5), Point(2, 2))
    rec.draw(win)

    # Enter loop to accept mouse clicks while BMI has not been calculated.
    gui_quit = False
    while not gui_quit:
        clickPoint = win.getMouse()
        clickPointY = clickPoint.getY()
        clickPointX = clickPoint.getX()
        try:
            height = int(heightFtInput.getText()) * 12 + int(heightInInput.getText())
            weight = int(weightInput.getText())
            bmi = 703 * weight / height ** 2
            result = bmi_category(bmi)[0]
            fontColor = bmi_category(bmi)[1]
            outString = str(bmi) + "\n" + result
        except ValueError:
            continue

        if not gui_quit:
            if 1.5 <= clickPointY <= 2 and 1 <= clickPointX <= 2:
                output.setText(str(outString))
                output.setOutline(fontColor)
                button.setText("Quit")
                gui_quit = True
            else:
                continue
    # Enter loop to allow clicks after BMI has been calculated.
    # Users are now able to quit.
    while gui_quit:
        quitClickPoint = win.getMouse()
        quitClickPointY = quitClickPoint.getY()
        quitClickPointX = quitClickPoint.getX()
        if gui_quit:
            if 1.5 <= quitClickPointY <= 2 and 1 <= quitClickPointX <= 2:
                win.close()
                break

main()
