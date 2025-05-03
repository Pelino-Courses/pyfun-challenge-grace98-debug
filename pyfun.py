from typing import List, Iterator
from abc import ABC, abstractmethod

# Abstract Person class
class Person(ABC):
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self.name = name

    @abstractmethod
    def get_role(self) -> str:
        pass

# Student class
class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.enrollments: List["Course"] = []

    def get_role(self):
        return "Student"

    def enroll(self, course: "Course"):
        self.enrollments.append(course)
        course.students.append(self)

    def __iter__(self) -> Iterator["Course"]:
        return iter(self.enrollments)

# Instructor class
class Instructor(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.courses: List["Course"] = []

    def get_role(self):
        return "Instructor"

# TA with multiple inheritance
class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str):
        Student.__init__(self, name)
        Instructor.__init__(self, name)

    def get_role(self):
        return "Teaching Assistant"

# Course class
class Course:
    def __init__(self, name: str):
        self.name = name
        self.students: List[Student] = []

    def __iter__(self) -> Iterator[Student]:
        return iter(self.students)

    def __add__(self, other: "Course") -> List[Student]:
        return list(set(self.students + other.students))

    @classmethod
    def create(cls, name: str) -> "Course":
        return cls(name)

# Example usage
s = Student("Grace")
ta = TeachingAssistant("Pelino")
c1 = Course.create("Python")
c2 = Course.create("Coding")

s.enroll(c1)
ta.enroll(c1)
ta.enroll(c2)

print(f"{s.name}'s courses:", [c.name for c in s])
print(f"Students in {c1.name}:", [st.name for st in c1])
print("Combined:", [st.name for st in c1 + c2])
