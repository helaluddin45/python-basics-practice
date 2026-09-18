class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_info(self):
        return f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}"

    def is_pass(self):
        average = sum(self.marks) / len(self.marks)
        if average >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Saida", 101, [85, 90, 78, 92])
print(student1.display_info())
print("Result:", student1.is_pass())

