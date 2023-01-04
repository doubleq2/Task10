from fastapi import Depends, FastAPI
from core.db import *
import crud
from micro import models
from sqlalchemy.orm import Session
from typing import Union
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/cp")
def get_people_on_cource(db: Session = Depends(get_db)):
    res = crud.get_groups_people(db)
    return res


@app.get("/sc")
def get_student_by_cource(cource_name:str,db: Session = Depends(get_db)):
    res = crud.get_student_by_cource(db,cource_name)
    return res

@app.delete("/student")
def del_student(student_id:str,db: Session = Depends(get_db)):
    student = crud.delete_student(db,student_id) 
    return student

@app.post("/students/")
def inst_student(new_student_id:int,first_name:str,last_name:str,new_group_id:Union[int, None] = None,db: Session = Depends(get_db)):
    student = crud.post_student(db,new_student_id,new_group_id,first_name,last_name) 
    return student

@app.post("/student/cource")
def inst_student_to_cource(student_id:int,cource_id:int,db: Session = Depends(get_db)):
    student_info = crud.post_student_to_cource(db,student_id,cource_id)
    return student_info

@app.delete("/del_student")
def del_student_from_cource(student_id:int,cource_id:int,db: Session = Depends(get_db)):
    student_info = crud.delete_student_from_cource(db,student_id,cource_id)
    return student_info