from fastapi import FastAPI

app = FastAPI() # Create an instance of the FastAPI application


@app.get("/") # Define a route: when someone visits GET / (the root), this function runs
def read_root():
    return {"message": "Welcome ti Kitty's Foraging Log API"} # Returns a simple JSON response
