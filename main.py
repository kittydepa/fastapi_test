from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import date


# Create an instance of the FastAPI application
app = FastAPI()

# Temporary in-memory storage for forage items
fake_db = []


# Defining a new data model called ForageItem, which inherits from BaseModel, so FastAPI knows how to parse, validate, and document it
class ForageItem(BaseModel):
    id: int = Field(..., example=1, description="Unique ID for the item")
    name: str = Field(..., example="Chanterelle", description="Name of the mushroom or berry")                                     # Because `id` is required, the `...` means no default value
    type: str = Field(..., example="mushroom", description="Either 'mushroom' or 'berry'")                                         # `example` is used in documentation (like Swagger or Redoc)
    location: str = Field(..., example="Grimsta Naturreservat", description="Where it was found")                                  # `description`shows up in the OpenAPI schema
    date: date = Field(..., example="2025-07-21", description="Date of the foraging event")
    is_edible: bool = Field(..., example=True, description="Whether the item is safe to eat")
    notes: Optional[str] = Field(None, examples="Found under pine trees", description="Extra notes")
    photo_url: Optional[HttpUrl] = Field(None, examples="https://example.com/photo.jpg", description="Optional image link")


# Define a route: when someone visits GET / (the root), this function runs
@app.get("/")
def read_root():
    return {"message": "Welcome ti Kitty's Foraging Log API"} # Returns a simple JSON response
