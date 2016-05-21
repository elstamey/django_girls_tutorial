with open('newtext.txt', 'w') as new:
    print('this is a new line of text')
    print('another line of text')
    new.write('this is a new line of text\n')
    new.write('another line of text\n')
    new.close()
