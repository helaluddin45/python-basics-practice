class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_info(self):
        return f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}"

    def total_marks(self):
        return sum(self.marks)


student1 = Student("Saida", 101, [85, 90, 78, 92])
print(student1.display_info())
print("Total Marks:", student1.total_marks())
