### ========== Library ========== ###
from fastapi import HTTPException, status
from config.database import studentsCollection
from utilities.utilities import convertStudent, convertStudents
from bson import ObjectId

### ========== Define Controllers ========== ###

def home():
    return {
        "status": "Ok",
        "message": "Connect Successful! :))"
    }


def create(student):
    studentsCollection.insert_one(dict(student))
    return {
        "status": "Ok",
        "message": "Student inserted successful!",
        "data": dict(student)
    }


def getAll():
    students = studentsCollection.find()
    students = convertStudents(students)
    return {
        "status": "Ok",
        "data": students
    }


def getId(id):
    student = studentsCollection.find_one({"_id": ObjectId(id)})

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found student with id {id}"
        )
    
    student = convertStudent(student)

    return {
        "status": "Ok",
        "data": student
    }


def update(id, student):
    student_ = studentsCollection.find_one({"_id": ObjectId(id)})

    if student_ is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found student with id {id}"
        )
    
    studentsCollection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(student)}
    )

    return {
        "status": "Ok",
        "message": "student has been updated successfully!"
    }


def delete(id):
    student_ = studentsCollection.find_one({"_id": ObjectId(id)})

    if student_ is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found student with id {id}"
        )
    
    studentsCollection.find_one_and_delete({"_id": ObjectId(id)})

    return {
        "status": "Ok",
        "message": "student has been deleted successfully!"
    }