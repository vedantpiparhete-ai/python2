class InvalidMarksError(Exception):
    pass

def acceptMarks(a, b, c):
    if (a < 0 or a > 100) or (b < 0 or b > 100) or (c < 0 or c > 100):
        raise InvalidMarksError("Out of Range")
    else:
        total = a + b + c
        per = (total / 300) * 100  # Fixed the '-' to '=' and added grouping parentheses
        print('Total: ', total)
        print('Percentage: ', per)

# Input section
a = int(input('Enter marks for Python: '))
b = int(input('Enter marks for Java: '))
c = int(input('Enter marks for C: '))

# Exception handling block
try:
    acceptMarks(a, b, c)
except InvalidMarksError as e:
    print(e)