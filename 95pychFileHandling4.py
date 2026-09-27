with open('Text File3.txt','w')as f:
    f.write('****** Programming')
    print(f.tell())
    f.seek(0)
    f.write('Pyrthon')
    f.seek(50)
    f.write('Hellow')