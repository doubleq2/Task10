from core.db import *
from micro.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dan import *
import random

engine = create_engine("postgresql+psycopg2://qq224:123@localhost/ts10")
session = sessionmaker(bind=engine)
db = session()

try:
    for namey in group:
        db.add(Group(name=namey))
        db.commit()
    for fulname in people:
        sf = fulname.split()
        db.add(Student(group_id=gen(random.randint(0,1)),first_name=sf[0],last_name=sf[1]))
        db.commit()
    for nameg in sublist:
        db.add(Cource(name=nameg,decription=f"Это всего лишь {nameg}."))
        db.commit()
    for student_id in range(200):
        for _ in range(random.randint(1,3)):
            student = db.query(Student).all()[student_id]
            cource = db.query(Cource).all()[random.randint(0,9)]
            student.cources.append(cource)
            db.commit()
            
finally:
    db.close()
    print("cl")