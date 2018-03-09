def getStudents():
    Students = ["Bharat" , "Ashish"]
    def getStudentsTitle():
        Students_TitleCases=[]
        for students in Students:
            Students_TitleCases.append(students.title())
            return Students_TitleCases

    Students_titleCases_names=getStudentsTitle()
    print (Students_titleCases_names)
