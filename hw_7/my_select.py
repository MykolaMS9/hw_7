from datetime import datetime

from sqlalchemy.orm import joinedload, subqueryload
from sqlalchemy import and_, or_, func, desc, asc, select

from hw_7.src.db import session
from hw_7.src.models import Student, Grade, Group, Teacher, Discipline


def select_01():
    res = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.fullname).order_by(desc('avg_grade')).limit(5).all()
    return res


def select_02(value: int):
    res = (session.query(
        Discipline.name,
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
           .select_from(Grade) \
           .join(Student) \
           .join(Discipline) \
           .filter(Discipline.id == value) \
           .group_by(Student.fullname, Discipline.name) \
           .order_by(desc('avg_grade')) \
           .limit(1).all())
    return res


def select_03(value: int):
    res = (session.query(
        Discipline.name,
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
           .select_from(Grade) \
           .join(Student) \
           .join(Discipline) \
           .join(Group) \
           .filter(Discipline.id == value) \
           .group_by(Group.name, Discipline.name) \
           .order_by(desc('avg_grade')) \
           .all())
    return res


def select_04():
    res = (session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
           .select_from(Grade) \
           .all())
    return res


def select_05(value: int):
    res = (session.query(
        Teacher.fullname,
        Discipline.name
    ) \
           .select_from(Discipline) \
           .join(Teacher) \
           .filter(Teacher.id == value) \
           .group_by(Teacher.fullname, Discipline.name) \
           .order_by(asc(Teacher.fullname)) \
           .all())
    return res


def select_06(value: int):
    res = (session.query(
        Student.fullname,
        Group.name
    ) \
           .select_from(Student) \
           .join(Group) \
           .filter(Group.id == value) \
           .group_by(Student.fullname, Group.name) \
           .order_by(asc(Group.name)) \
           .all())
    return res


def select_07(g_id: int, d_id):
    res = (session.query(
        Student.fullname,
        Group.name,
        Grade.grade,
        Grade.date_of,
        Discipline.name,
    ) \
           .select_from(Grade) \
           .join(Student) \
           .join(Discipline) \
           .join(Group) \
           .filter(and_(Group.id == g_id, Discipline.id == d_id)) \
           .order_by(asc(Grade.date_of)) \
           .all())
    return res


def select_08(t_id: int):
    res = (session.query(
        Discipline.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade'),
        Teacher.fullname
    ) \
           .select_from(Grade) \
           .join(Discipline) \
           .join(Teacher) \
           .filter(Teacher.id == t_id) \
           .group_by(Discipline.name, Teacher.fullname) \
           .order_by(asc(Discipline.name)) \
           .all())
    return res


def select_09(s_id: int):
    res = (session.query(
        Discipline.name,
        Student.fullname,
    ) \
           .select_from(Grade) \
           .join(Discipline) \
           .join(Student) \
           .filter(Student.id == s_id) \
           .group_by(Discipline.name, Student.fullname) \
           .order_by(asc(Discipline.name)) \
           .all())
    return res


def select_10(s_id: int, t_id: int):
    res = (session.query(
        Discipline.name,
        Student.fullname,
        Teacher.fullname,
    ) \
           .select_from(Grade) \
           .join(Discipline) \
           .join(Student) \
           .join(Teacher) \
           .filter(and_(Student.id == s_id, Teacher.id == t_id)) \
           .group_by(Discipline.name, Student.fullname, Teacher.fullname) \
           .order_by(asc(Discipline.name)) \
           .all())
    return res


def select_11(s_id: int, t_id: int):
    res = (session.query(
        Teacher.fullname,
        Student.fullname,
        Discipline.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade'),
    ) \
           .select_from(Grade) \
           .join(Discipline) \
           .join(Student) \
           .join(Teacher) \
           .filter(and_(Student.id == s_id, Teacher.id == t_id)) \
           .group_by(Discipline.name, Student.fullname, Teacher.fullname) \
           .order_by(asc(Discipline.name)) \
           .all())
    return res


def select_12(d_id, grou_id: int):
    subquery = (select(
        Grade.date_of
    ) \
                .join(Student) \
                .join(Group) \
                .where(and_(Grade.discipline_id == d_id, Group.id == grou_id)) \
                .order_by(desc(Grade.date_of)) \
                .limit(1).scalar_subquery())
    res = (session.query(
        Discipline.name,
        Student.fullname,
        Group.name,
        Grade.date_of,
        Grade.grade,
    ) \
           .select_from(Grade) \
           .join(Discipline) \
           .join(Student) \
           .join(Group) \
           .filter(and_(Discipline.id == d_id, Group.id == grou_id, Grade.date_of == subquery)) \
           .group_by(Discipline.name, Student.fullname, Group.name, Grade.date_of, Grade.grade) \
           .order_by(desc(Grade.date_of)) \
           .all())
    return res


if __name__ == '__main__':
    # select_01 ------------------------

    # for val in select_01():
    #     print(val)

    #     select_02-------------------------

    # res = [select_02(id_) for id_ in range(1, 9)]
    # for r in res:
    #     print(r)

    #     select_03-------------------------

    # res = [select_03(id_) for id_ in range(1, 9)]
    # for r in res:
    #     print(r)

    #     select_04-------------------------

    # for val in select_04():
    #     print(val)

    #     select_05-------------------------

    # res = [select_05(id_) for id_ in range(1, 6)]
    # for r in res:
    #     print(r)
    #
    #     select_06-------------------------

    # res = [select_06(id_) for id_ in range(1, 4)]
    # for r in res:
    #     print(r)
    #
    #     select_07-------------------------

    # res = [select_07(g_id, d_id) for g_id in range(1, 4) for d_id in range(1, 9)]
    # for r in res:
    #     print('-'*50)
    #     for r_ in r:
    #         print(r_)
    #
    #     select_08-------------------------

    # res = [select_08(id_) for id_ in range(1, 6)]
    # for r in res:
    #     print(r)

    #     select_09-------------------------

    # res = [select_09(id_) for id_ in range(1, 51)]
    # for r in res:
    #     print('-'*50)
    #     for r_ in r:
    #         print(r_)

    # select_10-------------------------

    # res = [select_10(s_id, t_id) for s_id in range(1, 50) for t_id in range(1, 6)]
    # for r in res:
    #     print('-'*150)
    #     for r_ in r:
    #         print(r_)

    # select_11-------------------------

    # res = [select_11(s_id, t_id) for s_id in range(1, 50) for t_id in range(1, 6)]
    # for r in res:
    #     print('-'*150)
    #     for r_ in r:
    #         print(r_)

    # select_12-------------------------

    res = [select_12(d_id, grou_id) for d_id in range(1, 9) for grou_id in range(1, 4)]
    for r in res:
        print('-' * 150)
        for r_ in r:
            print(r_)
