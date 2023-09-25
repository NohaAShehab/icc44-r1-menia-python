

try:
    fileobject = open('users.txt', 'r')

except Exception as e:
    print(e)

else:
    # print(fileobject)
    # data = fileobject.read()  # read file content into one string
    # print(data, type(data))
    # # data = data.split('\n')
    # # print(data)
    #

    # read file line by line
    # fileobject.seek(0)
    lines = fileobject.readlines()  # read file content line by line a list
    print(lines, type(lines))
    fileobject.close()

    # print(fileobject.read())