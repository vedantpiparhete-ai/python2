def aoc(rad):
    return 3.14*rad*rad

def coc(rad):
    return 2*3.14*rad

r=int(input("Enter radius: "))
acrircle=aoc(r)
print("Area",acrircle)
cir=coc(r)
print("Circumference of circle: ",cir)