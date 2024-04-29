# Import necessary modules and types
from typing import Union
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root URL "/"
@app.get("/")
def read_root():
    # Define a function to handle GET requests to the root URL
    # This function returns a dictionary with a message
    return {"Hello Pakistan this is abdul qadir": "World"}

# Define a route for the "/items/{item_id}" endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # Define a function to handle GET requests to the "/items/{item_id}" endpoint
    # This function takes two parameters: item_id (an integer) and q (an optional string or None)
    # This function returns a dictionary with the item_id and q parameters
    return {"item_id": item_id, "q": q}