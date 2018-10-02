'''
MEMBERS
Opio Arthur Moses 
Registration Number:

Jonathan Mukiibi: 
Registration Number: 2018/HD05/1968U

Omara Patrick: Student Number:216018844 
Registration Number: 2016/HD05/339U

Jerome Abura: Student Number: 203001168 
Registration Number: 2014/HD05/2094U

Wabwire Robert: Student Number: 2018/HD05/1982U
'''

class Student:
    def __init__(self,firstname,lastname,regno,gradeaverage,regyear):
        self.firstname = firstname
        self.lastname = lastname
        self.regno = regno
        self.gradeaverage = gradeaverage
        self.regyear=regyear

    def tostring(self):
        description = self.lastname + ', ' + self.firstname + '. \Registration number ' + self.regno + ',' + self.gradeaverage +' \Registration Year '+ self.regyear
        return description
    
    def setgrade(self,gradeaverage):
        self.gradeaverage = gradeaverage
        return gradeaverage

class MasterStudent(Student):
    def __init__(self,status):
       self.status=status

    def tostring(self):
        return self.status
         
    
class Course:
    def __init__(self,coursetitle):
        self.coursetitle = coursetitle
        self.students = []
        self.lecturers = []
        

    def addstudent(self,newstudent):
        self.students.append(newstudent)
        
    def addlecturer(self,newlecturer):
        self.lecturers.append(newlecturer)
    
    def tostring(self):
        str = self.coursetitle + '\n'
        str = str + 'Students enrolled:\n'
        for s in self.students:
            str = str + s.tostring() + '\n'

        for s in self.lecturers:
            str = str + s.tostring() + '\n'
        return str
    
class Lecturer:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def tostring(self):
            description = self.lastname + ', ' + self.firstname
            return description
    
#creating instances
student1 = Student('Jimi','Hendrix','123456','45','2018')
student2 = Student('Frank','Zappa','234567','70','2018')
student3 = Student('Ringo','Starr','345678','55','2018')
lecturer1 = Lecturer('Engineer','Bainomugisha')

course1 = Course('MSc Computer Science')
course1.addstudent(student1)
course1.addlecturer(lecturer1)
course1.addstudent(student2)
course1.addstudent(student3)
newaverage=student1.setgrade('70')
masters= MasterStudent('This is a masters student')
print(masters.tostring())


print ('The new average is ' + newaverage)

print (course1.tostring())
