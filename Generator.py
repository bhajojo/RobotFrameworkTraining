students= []

def read_file():
    try:
        f= open("students.txt","r")
        for student in read_students(f):
            students.append(student)
            f.close()
    except Exception:
        print ("Could not read the file ")

read_file()

def read_students(f):
    for line in f:
        yield line
print (students)


