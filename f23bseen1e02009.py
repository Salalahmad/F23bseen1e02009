class SchemeOfStudy:
    def _init_(self, name, subjects):
        self.name = name
        self.subjects = subjects
    def _str_(self):
        return f"{self.name} ({','.join(self.subjects)})"
class Student:
    def _init_(self, name):
        self.name = name
        self.scheme = None
    def apply_scheme(self, scheme):
        self.scheme = scheme
    def _str_(self):
        return f"Student: {self.name}, Scheme: {self.scheme or 'No scheme'}"
class Class:
    def _init_(self, name):
        self.name = name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def apply_scheme(self, scheme):
        for student in self.students:
            student.apply_scheme(scheme)
    def _str_(self):
        students_info = "\n  ".join(str(student) for student in self.students)
        return f"Class: {self.name}  Students:  {students_info}"
class Section:
    def _init_(self, name):
        self.name = name
        self.classes = []
    def add_class(self, class_):
        self.classes.append(class_)
    def apply_scheme(self, scheme):
        for class_ in self.classes:
            class_.apply_scheme(scheme)
    def _str_(self):
        classes_info = "\n  ".join(str(class_) for class_ in self.classes)
        return f"Section: {self.name}  Classes:  {classes_info}"
scheme1 = SchemeOfStudy("Science", ["Physics", "Chemistry", "Biology"])
scheme2 = SchemeOfStudy("Programming", ["OOP", "DSA", "DBMS"])
student1 = Student("Ali")
student2 = Student("Ahmad")
student3 = Student("Umar")
class1 = Class("2nd-1E")
class1.add_student(student1)
class1.add_student(student2)
class2 = Class("2nd-2E")
class2.add_student(student3)
section1 = Section("Section 1")
section1.add_class(class1)
section1.add_class(class2)
student1.apply_scheme(scheme1)
print(student1)
print()
class2.apply_scheme(scheme2)
print(class2)
print()
section1.apply_scheme(scheme1)
print(section1)