def square_less_than_fifty(x):
    square = x ** 2
    if square < 50:
        return None
    else:
        print(square)
        return square

x = int(input('Please enter an integer:'))
square_less_than_fifty(x)
