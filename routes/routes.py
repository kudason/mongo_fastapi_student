### ========== Library ========== ###
from fastapi import APIRouter
from models.student import Student
from controllers import controllers

### ========== Define Router ========== ###
router = APIRouter(tags=['Students'])

### ========== Create function ========== ###

### get root entry ###
@router.get("/")
def root_entry():
    return controllers.home()

### Create a new student ###
@router.post('/student')
def create_student(student: Student):
    return controllers.create(student)

### Get all students ###
@router.get('/student')
def get_all_students():
    return controllers.getAll()

### Get student by id ###
@router.get('/student/{id}')
def get_student_by_id(id: str):
    return controllers.getId(id)

### Update student ###
@router.put('/student/{id}')
def update_student(id: str, student: Student):
    return controllers.update(id, student)

### Delete student ###
@router.delete('/student/{id}')
def delete_student_by_id(id: str):
    return controllers.delete(id)