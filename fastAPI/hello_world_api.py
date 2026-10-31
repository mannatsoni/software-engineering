# fastapi class from fastapi
from fastapi import FastAPI
import time

# create an instance of the FastAPI class
app = FastAPI()

# define a route for the root endpoint
@app.get("/")
# build a method for this endpoint
def hello_world():
    return {"message": "Hello, World!", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

# to run this code, use the command: uvicorn hello_world_api:app --reload

# about endpoint to give information about the API
@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application that returns a greeting message."}