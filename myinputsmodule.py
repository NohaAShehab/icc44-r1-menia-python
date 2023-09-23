num = 10

def askforInt(message):
    while True:
        num  = input(message)
        if num.isdigit():
            return int(num)

        print('===please enter valid number ====')


def askforpurealphas(message):
    while True:
        inputt = input(message)
        if inputt.isalpha():
            return inputt

        print('---- not valid input -----')
if __name__=='__main__':
    age  = askforInt('please enter age: ')
    print(age)