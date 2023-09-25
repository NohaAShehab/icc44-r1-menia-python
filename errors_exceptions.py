

"""
    syntax errors: parser --> must solve it
    logical errors: --> must be solved by developer
    runtime errors: --->  unexpected action caused the process (program) to stop


"""

# def sumnum(num1, num2):
#     res = num1 * num2
#     print(res)
#
# sumnum(2,2)
# sumnum(3,4)


""" runtime errors """


# print(name)  # Name Error

# print(6/0)  # ZeroDivisionError

# age = int(input('please enter age: '))
# print(age) #ValueError
#



# Exception handling


# try:
#     print(name)
# except:
#     print("---- problem happened----- ")
#     name = ''
#
#
#
# name +='iti'

""
# try:
#     print(name)
# except:
#     print("---- error with process----- ")
#     exit()


# try:
#     # print(name)
#     # print(34/0)
#     num = int(input('----: '))
# except NameError as ne:
#     print(f'=--problem happened {ne}')
#     name = ''
# except ZeroDivisionError as ze:
#     print(ze)
#     res = 0
# except TypeError:
#     print('--invalid types')
# except Exception as e:
#     print(e)
#     # exit(1)
#
# else:
#     # dependent process --> will be executed only if there is no problem in the try block
#     print(num)
#     num +=10
#     print(num)
#
# finally:
#     print("---- bye ------")




def askforInt():
    done = False
    try:
        num = int(input('please enter number: '))
    except Exception as e:
        print(e)
        return  None
    else:
        done  =  True
        return num
    finally:
        """ execution finally precedes return in function """
        if done:
            print("--- valid input int ---")
        else:
            print("--- invalid input ")

        # return done
    # if done:
    #     print("--- valid input int ---")
    # else:
    #     print("--- invalid input ")


res = askforInt()
print(res)

#
# done = False
# while True:
#     try:
#         num = int(input('please enter number: '))
#     except Exception as e:
#         print(e)
#         continue
#     else:
#         done  =  True
#         break
#     finally:
#         """ execution finally precedes break in loop """
#         if done:
#             print("--- valid input int ---")
#         else:
#             print("--- invalid input ")
