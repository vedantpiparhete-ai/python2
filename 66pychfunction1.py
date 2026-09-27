def aoc(rad):
    return 3.14*rad*rad

def coc(rad):
    return 2*3.14*rad

r=int(input("Enter radius of circle: "))
print("Area of circle: ",aoc(r))
print("Circumference of circle: ",coc(r))