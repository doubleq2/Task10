from sqlalchemy import Column, String, Integer, ForeignKey, Table
from core.db import Base
from sqlalchemy.orm import relationship


association_table = Table(
    "ahahahahah",
    Base.metadata,
    Column("Cource_id",Integer,ForeignKey("cources.id",ondelete="CASCADE",onupdate="CASCADE"), primary_key=True),
    Column("Student_id",Integer,ForeignKey("students.id",ondelete="CASCADE",onupdate="CASCADE"), primary_key=True),
)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    Student = relationship("Student")
    
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    group_id = Column(Integer, ForeignKey("groups.id",ondelete="CASCADE",onupdate="CASCADE"))
    first_name = Column(String)
    last_name = Column(String)
    cources = relationship("Cource", secondary=association_table, back_populates="students")
    
class Cource(Base):
    __tablename__ = 'cources'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    decription = Column(String)
    students = relationship("Student", secondary=association_table, back_populates="cources")