
"""w  --> open file for writing ?
    when you try to open file for writing ---> and file
    doesn't exist --> python will try to create it ?

    when you open file with write mode --> open file for writing
    starting from the beginning of the file ?
"""
try:
    fileobject = open('mycv.txt', 'w')

except Exception as e:
    print(e)

else:
    print(fileobject)
    fileobject.write('python is easy\n')
    fileobject.write('---Files is simple -----')
    fileobject.write('''My name is Noha
I works at iti''')

    fileobject.writelines(['Ahmed', 'Mohamed', 'Ali', 'test'])  # accept iterable of strings.
    fileobject.close()

