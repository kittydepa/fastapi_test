# Step-by-step instructions

## Setup

See the [README](./README.md#setup) file for the required setup.

## Testing out `fastapi` and `uvicorn`

1. Set up your FastAPI by creating your `main.py` file.

    **Tip**: You can start with something simple, such as:

    ```python
    # main.py
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")

    def read_root():
        return {"message": "This is YOUR API!"}
    ```

1. From the terminal, in the same folder where `main.py` is located, run the following command:

    ```bash
    uvicorn main:app --reload
    ````

    If the script was successful, you can try opening your browser to:

    * http://localhost:8000 - shows the welcome message.

    * http://localhost:8000/docs - shows your API in Swagger UI

    * http://localhost:8000/redoc - shows your API in Redoc UI

## Add a Pydantic model for `ForageItem`

1. In your `main.py` file, add to the top, below the FastAPI import:

    ```python
    from pydantic import BaseModel, Field, HttpUrl
    from typing import Optional
    from datetime import date
    ```

    * `BaseModel` is the the "core" of Pydandic. All your data models inherit from it.

    * `Field()` lets your customise descriptions, examples, and validation.

    * `HttpUrl` ensures that only valid URLs are provided for image links.

    * `Optional[...]` lets you declare if a field is optional.

    * `date` allows you to store calendar dates, as a `date` data type, not just as a string (`str`)

1. Define the `ForageItem` model:

...

## Create basic `/items` endpoint to **POST** new items and **GET** all items

* Create an empty list to act as a "fake" database

* Define `POST /items` route

* Use the `ForageItem` model to validate incoming data

* Add the new item to the list and return it

