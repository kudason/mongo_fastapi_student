### ========== Convert Student to dict() tyoe ========== ###
def convertStudent(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"],
        "gpa": student["gpa"]
    }

### ========== Convert a list of Student to dict() type ========== ###
def convertStudents(students) -> list:
    return [convertStudent(student) for student in students]