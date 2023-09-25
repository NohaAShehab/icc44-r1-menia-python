

## buil-in modules ?



import  os
#
# print(os.getcwd())  # pwd
#
# print(os.getlogin())
# print(os.getenv('path'))
#
# # os.mkdir('test')
#
# os.rmdir('test')


import math
# print(math.pi)



import re


def askforEmail(message = 'please enter your mail'):
    pattern =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-._]+\.[A-Z|a-z]{2,7}\b'
    while True:
        email = input(message)
        # vallidate emaill ?
        """ if input follow pattern ? match object : None """
        # valid_email = re.match(pattern, email)  # match function returns with match object if the part of the string follows the pattern
        valid_email= re.fullmatch(pattern, email)
        if valid_email:
            return  email, valid_email
        print(f"---- incorrect input please re-enter it again ----, {valid_email}")




"noha@iti-gov-eg.comm"

# myemail=askforEmail()
# print(myemail)



""" password at least 8 chars, upper + lower case char, special chars, numbers ---> regex"""

""" validation phone number  --> python library ---> regex"""



""" json  """

import  json
info = {'id':1, "name": "noha"}
info=json.dumps(info)  # convert any object to string
print(info)

users = json.dumps(['44',44,'ahmed', 'ffff'])
print(users)


'string  ---> return to its datatype '


users_data = json.loads(users)
print(users_data)


