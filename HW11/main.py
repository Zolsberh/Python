from typing import Dict
from student import Student
import json


def get_dict_student(student: Student) -> Dict:

    dict_student = {
        'firstname': student.firstname,
        'lastname': student.lastname,
        'age': student.age,
        'group': student.group
    }
    return dict_student


def get_student(dict_student: Dict) -> Student:

    student = Student(
        dict_student['firstname'],
        dict_student['lastname'],
        dict_student['age'],
        dict_student['group']
    )
    return student


file = 'student.json'
st = Student('Иван', 'Иванов', 25, 'Python228')

with open(file, 'w') as js_file:
    d = get_dict_student(st)
    json.dump(d, js_file,  ensure_ascii=False, indent=4)

with open(file, 'r') as js_file:
    d = json.load(js_file)
    st2 = get_student(d)

print(st2)
