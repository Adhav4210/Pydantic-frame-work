from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    email: str
user = User(id=1, name="John Doe", email="adhav4210@gmail.com")
print(user)
