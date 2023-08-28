import csv
with open("test.csv","r") as obj:
    fobj = csv.reader(obj)
    for i in fobj:
        if i[1] != " state = 'EYE_FOUND'":
            print("Not Successful")
            obj.close()
            exit()
        else:
            pass
    obj.close()
print("Successful!")
