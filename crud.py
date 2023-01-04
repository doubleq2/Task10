from sqlalchemy.orm import Session
from micro import models


def get_groups_people(db:Session):
    res = []
    name_cources = []
    cources = db.query(models.Cource.name).all()
    for i in cources:
        name_cources.append(i["name"])
    for i in range(len(name_cources)):
        cource_id = i+1
        cource = db.query(models.Cource).filter(models.Cource.id == cource_id).first()
        b = cource.students
        a = name_cources[i]
        sl = {}
        sl[a]=b
        res.append(sl)
    return res


def get_student_by_cource(db:Session,cource_name):
    cource = db.query(models.Cource).filter(models.Cource.name == cource_name).first()
    sd = cource.students
    return sd

def delete_student(db:Session,student_id):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    db.delete(student)
    db.commit()
    return db.query(models.Student).all()

def post_student(db:Session,new_student_id,new_group_id,first_name,last_name):
    new_student = models.Student(id = new_student_id,group_id=new_group_id,first_name=first_name,last_name=last_name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return db.query(models.Student).all()

def post_student_to_cource(db:Session,student_id,cource_id):
    student = db.query(models.Student).all()[student_id-1]
    cource = db.query(models.Cource).all()[cource_id-1]
    student.cources.append(cource)
    db.commit()
    return student.cources

def delete_student_from_cource(db:Session,student_id,cource_id):
    student = db.query(models.Student).all()[student_id-1]
    cource = db.query(models.Cource).all()[cource_id-1]
    student.cources.remove(cource)
    db.commit()
    return student.cources