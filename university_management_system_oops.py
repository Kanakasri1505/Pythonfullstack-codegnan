####university management system using oops

class person:
    university="vignan_university"
    def __init__(self,name,age,gender,edu_back,dept):
        self.name=name
        self.age=age
        self.gender=gender
        self.edu_back=edu_back
        self.dept=dept
    def display_info(self):
        pass

class student(person):
    stu_count=0
    def __init__(self,name,age,gender,year,edu_back,dept,student_id):
        super().__init__(name,age,gender,edu_back,dept)
        self.__student_id=student_id
        self.year=year
        student.stu_count+=1
        
    def display_info(self):
        print("STUDENT DETAILS:")
        print(f"Name: {self.name} \n Age: {self.age} \n Gender: {self.gender}\n Educational_background: {self.edu_back} \n Department: {self.dept} \n Year: {self.year}")

    def get_id(self):
        print(f"private attribute: student_id : {self.__student_id}")
    def count(self):
        return student.stu_count
    
class faculty(person):
    faculty_count=0
    def __init__(self,name,age,gender,edu_back,dept,faculty_id,experience):
        super().__init__(name,age,gender,edu_back,dept)
        self.__faculty_id=faculty_id
        self.experience=experience
        faculty.faculty_count+=1
        
    def display_info(self):
        print("FACULTY DETAILS:")
        print(f"Name: {self.name} \n Age: {self.age} \n Gender: {self.gender}\n Educational_background: {self.edu_back} \n Department: {self.dept} \n Experience: {self.experience}")

    def get_id(self):
        print(F"private attribute : faculty_id : {self.__faculty_id}")

    def count(self):
        return faculty.faculty_count

student1=student(name="saranya",age=21,gender="Female",edu_back="intermediate",dept="ECE",year=4,student_id="22nm1456")
student2=student(name="arun",age=20,gender="male",edu_back="diploma",dept="CSE",year= 3 ,student_id="22nm2345" )
student3=student(name="ramya",age=21,gender="Female",edu_back="intermediate",dept="EEE",year= 4,student_id="22nm1567" )

faculty1=faculty(name="Sowmya",age=40,gender="Female",edu_back="PHD",dept="ECE",experience=6 ,faculty_id="fac123")
faculty2=faculty(name="srinivas",age=35,gender="male",edu_back="Mtech",dept="ECE",experience=4,faculty_id="fac345") 

student1.display_info()
student1.get_id()
student2.display_info()
student3.display_info()
print(f"student count: {student3.count()}")

faculty1.display_info()
faculty1.get_id()
faculty2.display_info()
print(f"faculty count: {faculty2.count()}")



              
    
    
