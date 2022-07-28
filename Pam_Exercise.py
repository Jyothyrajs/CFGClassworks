import random as rand

"""
Design a parent class called CFGStudent. It should have general attributes like name, surname, age, email, student id
and methods to fetch student's full name and student's id.
Important: there should be an option to pass student id when a new class object is generated, HOWEVER, if no id is
passed, then student_id should be automatically generated and assigned to the class.
"""


class CFGStudent:
    """blueprintprint for student info"""

    def __init__(self, first_name: str, surname: str, age: int, id = ""):
        # assert first_name != str, "Invalid input, enter alphabet characters only"
        # assert surname != str, "Invalid input, enter alphabet characters only"
        # assert age != int, "invalid input, please enter numerical values"
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.email = f"{first_name.lower()}.{surname.lower()}@cfg.com"
        self.student_id = id

    def full_name(self):
        """ put first name and last name together"""
        return self.first_name + " " + self.surname

    def generate_id(self):
        if self.student_id == '':
            self.student_id = str(rand.randint(1, 345))

        #     return self.student_id
        # else:
        #     return student_id

    def get_id(self):
        return self.student_id

    def display(self):
        print("Student Details")
        print(self.full_name())
        print(self.email)
        print(self.get_id())

"""
NanoStudent, which inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class, as well as additional two called 
'specialization' and 'course grades'

The child class 'generate_id' method should override its parent method to add the suffix 'NANO' in front of the id.
New methods 'add_new_grade' and 'get_course_grades' should be added.
"""


class NanoStudent(CFGStudent):
    # class inheriting parent class properties via super()
    def __init__(self, specialization, first_name, surname, age):
        super().__init__(first_name, surname, age)
        self.specialization = specialization
        self.course_grades = ""

    def generate_id(self):
        super().generate_id()
        self.student_id = "NANO"+super().get_id()

    def add_new_grade(self,grade):
        self.course_grades = grade

    def get_course_grades(self):
        return self.course_grades

    def display(self):
        print("Student Details")
        print(self.full_name())
        print(self.email)
        print(self.get_id())
        print(self.get_course_grades())

# """pass temp parameters to check code as you go along"""
student = CFGStudent("Pamela", "Mujikeni", 33)
student.generate_id()
student.display()

student = CFGStudent("Aneta", "Zepta", 25,"001")
student.generate_id()
student.display()

nano_stud = NanoStudent("S/W","Jyothy","Sobhana",38)
nano_stud.generate_id()
nano_stud.add_new_grade("A")
nano_stud.display()



