from sqlalchemy import Column, INTEGER, String, ForeignKey, DateTime, func, event, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(INTEGER, primary_key=True)
    fullname = Column(String(150), nullable=False)
    disciplines = relationship("Discipline", back_populates='teacher')


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(150), nullable=False)
    teacher_id = Column(INTEGER, ForeignKey('teachers.id', ondelete="CASCADE"))
    teacher = relationship("Teacher", back_populates='disciplines')
    grades = relationship("Grade", back_populates='discipline')


class Group(Base):
    __tablename__ = 'groups'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(150), nullable=False)
    students = relationship("Student", back_populates='group')


class Student(Base):
    __tablename__ = 'students'
    id = Column(INTEGER, primary_key=True)
    fullname = Column(String(150), nullable=False)
    group_id = Column(INTEGER, ForeignKey('groups.id', ondelete="CASCADE"))
    group = relationship("Group", back_populates='students')
    grades = relationship("Grade", back_populates='student')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(INTEGER, primary_key=True)
    grade = Column(INTEGER, nullable=False)
    date_of = Column(Date, nullable=False)
    student_id = Column(INTEGER, ForeignKey('students.id', ondelete="CASCADE"))
    student = relationship("Student", back_populates='grades')
    discipline_id = Column(INTEGER, ForeignKey('disciplines.id', ondelete="CASCADE"))
    discipline = relationship("Discipline", back_populates='grades')
