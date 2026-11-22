from dataclasses import dataclass


@dataclass
class Student:
    roll: str
    name: str
    marks: float


if __name__ == "__main__":
    student = Student("472", "Harshvardhan Singh", 85.5)
    print(student.roll, student.name, f"{student.marks:.1f}")
