from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Appliaction"}

@app.get("/sum")
async def sumOfTwoNumbers(a: int, b: int):
    return {"sum": a + b}

@app.get("/difference")
async def differenceOfTwoNumbers(a: int, b: int):
    return {"difference": a - b}



