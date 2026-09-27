with open('Text File4.txt', 'a') as f:
    while True:
        name = input('Enter task: ')
        if name.lower() == 'exit':
            break
        f.write(name)
        f.write('\n')
print('Done, Your task has been Added to the list Successfully!')