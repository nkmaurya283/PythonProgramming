

class Person:
    name=""
    age=0


    def __init__(self,person_name,pesrson_age):
        self.name=person_name
        self.age=pesrson_age

    def show_name(self):
        print(self.name)


    def show_age(self):
        print(self.age)


class Student(Person):
    studentID=""

    def __init__(self, student_name, student_age, student_id):
        super().__init__(student_name, student_age)
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # returns the value of student id


person1 = Person("Richard", 23)
# call member methods of the objects
person1.show_age()
# Create an object of the subclass
student1 = Student("Max", 22, "102")
print(student1.get_id())
student1.show_name()

