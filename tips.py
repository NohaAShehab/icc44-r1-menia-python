

# num =10
#
# while num > 0:
#     print(num)
#     num -=1


# ask user to enter numbers ---> once he enters string game over

# Never trust user input

# summ =0
# while True:
#     num =input('please enter num')
#     if num.isdigit():
#         num = int(num)
#         summ += num
#
#     else:
#
#         break  # break the loop
#
# print("--------Game Over-----")
# print(f'Your score is {summ}')


# for i in range(11):
#     if i==4:
#         continue  # skip current iteration
#
#     print(f'i ={i}')
#


# for i in range(11):
#     if i==4:
#         break
#
#     print(f'i ={i}')


''' program simulate atm password entering '''

for i in range(1, 4):
    password = input('please enter password: ')
    if password=='abc':
        print('logged in successfully')
        break

else:
    '''this block will be executed only if the loop reached its end '''
    print('===== your account has been blocked =======')


"""

    name='ahmed'
    if (name=='ahmed'){}
"""
name='ahmed'
if name=='ahmed':
    pass

print('-----------------')


for item in range(19):
    pass

