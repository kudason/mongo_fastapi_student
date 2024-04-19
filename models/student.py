### ========== Library ========== ###
from pydantic import BaseModel

### ========== Define student schema (response model) ========== ###
class Student(BaseModel):
    name: str
    age: int
    address: str
    gpa: float
       