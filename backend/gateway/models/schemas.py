from pydantic import BaseModel

class SignupSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str

class SigninSchema(BaseModel):
    username: str
    password: str

class UsersSchema(BaseModel):
    fullname: str
    phone: str
    email: str
    password: str
    role: int
    status: int

class TasksSchema(BaseModel):
    title: str
    description: str
    createdby: int
    assignedto: int
    priority: int
    deadline: str
    status: int