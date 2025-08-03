from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from typing import List
from datetime import date


# Create an instance of the FastAPI application
app = FastAPI()

# Temporary in-memory storage for forage items
fake_db = []


# Define a new data model called ForageItem, which inherits from BaseModel, so FastAPI knows how to parse, validate, and document it
class ForageItem(BaseModel):
    id_num: int = Field(..., example=1, description="Unique ID for the item")
    name: str = Field(..., example="Chanterelle", description="Name of the mushroom or berry")
    item_type: str = Field(..., example="mushroom", description="Either 'mushroom' or 'berry'")
    location: str = Field(..., example="Grimsta Naturreservat", description="Where it was found")
    date_found: date = Field(..., example="2025-07-21", description="Date of the foraging event")
    is_edible: bool = Field(..., example=True, description="Whether the item is safe to eat")
    notes: Optional[str] = Field(None, example="Found under pine trees", description="Extra notes")
    photo_url: Optional[HttpUrl] = Field(None, example="https://example.com/photo.jpg", description="Optional image link")


# Define a route
@app.post("/items", response_model=ForageItem, status_code=201)
def create_item(item: ForageItem):
    # Check for duplicates by ID
    if any(existing.id_num == item.id_num for existing in fake_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")

    # Add the item to the fake database
    fake_db.append(item)

    return item

# Add GET /items to return all entries
@app.get("/items", response_model=List[ForageItem])
def get_all_items():
    return fake_db

