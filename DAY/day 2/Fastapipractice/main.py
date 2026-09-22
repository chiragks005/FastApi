from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return{"page":"Home"}
@app.get("/about")
def about():
    return{"page":"About","author":"Rakesh"}
@app.get("/health")
def health():
    return {"Status":"ok"}
#postreq
@app.post("/create")
def create_some():
    return {"messege":"Created"}


#path
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result ":"Distinction","USN":usn}

@app.get("/candidate/{rollno}")
def get_date(rollno:int):
    return {"Result ":"Distinction","roll":rollno,"type":str(type(rollno))}

class Item(BaseModel):
    name : str
    price : float
    in_stock : bool = True
@app.post("/items")   
def create_item(item : Item):
    return {"received":item,"total_price":item.price*1.18}