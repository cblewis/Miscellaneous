import csv

with open('old.csv', 'r') as f1, open('new.csv', 'r') as f2, open('not in old.csv', 'w') as notinold, open('not in new.csv', 'w') as notinnew, open('test.csv', 'w') as test:
    fileone = f1.readlines()
    filetwo = f2.readlines()
    for line in filetwo:
        if line not in fileone:
            notinold.write(line)
    for line in fileone:
        if line not in filetwo:
            notinnew.write(line)
        if line in filetwo:
            test.write(line)
    notinold.close()
    notinnew.close()
    f1.close()
    f2.close()
