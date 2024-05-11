import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    @staticmethod
    def read_json(json_file):
        with open(json_file, 'r') as file:
            students_data = json.load(file)['students']
        students = []
        for student_data in students_data:
            student = Student(student_data['name'], student_data['age'], student_data['grades'])
            students.append(student)
        return students

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    @staticmethod
    def write_json(students, output_file):
        data = {}
        for student in students:
            data[student.name] = student.average_grade()
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        for student in students:
            print(f"{student.name}: {student.average_grade()}")

students = Student.read_json('data.json')
Student.write_json(students, 'average_grades.json')
