with open('read_me.txt', 'r') as text:
    for line in text:
        # print(line)
        print(line.strip())

# open() returns a file object, and is most commonly used with two arguments:
