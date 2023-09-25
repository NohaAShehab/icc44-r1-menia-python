
"""a --> open file for appending ?
    when you try to open file for writing ---> and file
    doesn't exist --> python will try to create it ?

    when you open file with append mode --> open file for writing
    starting from the end of the file
"""
try:
    fileobject = open('data.txt', 'a')

except Exception as e:
    print(e)

else:
    print(fileobject)
    fileobject.write('python is easy\n')
    fileobject.close()

