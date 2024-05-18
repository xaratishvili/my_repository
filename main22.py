import json
from faker import Faker
import random

fake = Faker()


def generate_student():
    return {
        "student_id": fake.uuid4(),
        "name": fake.name(),
        "age": random.randint(18, 24),
        "email": fake.email(),
        "is_active": random.choice([True, False])
    }


students = [generate_student() for _ in range(100)]

active_students = [student for student in students if student["is_active"]]
inactive_students = [student for student in students if not student["is_active"]]

students_json = {
    "active_students": active_students,
    "inactive_students": inactive_students
}

with open('students.json', 'w') as json_file:
    json.dump(students_json, json_file, indent=4)

