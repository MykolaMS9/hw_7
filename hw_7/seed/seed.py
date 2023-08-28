import random
from datetime import datetime, date, timedelta

from faker import Faker
from hw_7.src.db import session
from hw_7.src.models import Student, Teacher, Grade, Group, Discipline

fake = Faker('uk-UA')


def create_teachers():
    for _ in range(5):
        teacher = Teacher(
            fullname=f"{fake.first_name()} {fake.last_name()}",
        )
        session.add(teacher)
    session.commit()


def create_groups():
    groups = ['ET-01', 'IН-01', 'IТ-01']
    for val in groups:
        group = Group(
            name=val,
        )
        session.add(group)
    session.commit()


def create_disciplines():
    disciplines = [
        'Вища математика',
        "Дискретна математика",
        "Програмування",
        "Теорія основ електроенергетики",
        "Історія України",
        "Англійська мова",
        "Креслення",
        "Філософія"
    ]
    teachers = session.query(Teacher).all()
    for val in disciplines:
        teacher = random.choice(teachers)
        disc = Discipline(
            name=val,
            teacher_id=teacher.id
        )
        session.add(disc)
    session.commit()


def create_students():
    groups = session.query(Group).all()
    for _ in range(50):
        group = random.choice(groups)
        student = Student(
            fullname=f"{fake.first_name()} {fake.last_name()}",
            group_id=group.id
        )
        session.add(student)
    session.commit()


def get_list_date(start: date, end: date) -> list[date]:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result

def create_grades():
    students = session.query(Student).all()
    disciplines = session.query(Discipline).all()
    start_date = datetime.strptime('2023-09-01', "%Y-%m-%d")
    end_date = datetime.strptime('2024-06-15', "%Y-%m-%d")
    list_dates = get_list_date(start_date, end_date)
    for day in list_dates:
        disc = random.choice(disciplines)
        for _ in range(4):
            student = random.choice(students)
            grade = Grade(
                grade=random.randint(1, 5),
                date_of=day.date(),
                student_id=student.id,
                discipline_id=disc.id
            )
            session.add(grade)
    session.commit()


if __name__ == '__main__':
    create_teachers()
    create_groups()
    create_disciplines()
    create_students()
    create_grades()
