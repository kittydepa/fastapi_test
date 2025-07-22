# A Simple Foraging API

Making a simple API with FastAPI and **uvicorn**.
The main purpose is to try out FastAPI + documentation generation (with Redoc).

This API will be a simple foraging log, including information about mushrooms and berries you can forage in Sweden.

## Setup

Before you start, make sure you have the proper setup (especially if using VS Code with FastAPI), which includes:

* You have installed `fastapi` and `uvicorn`

* You have a `main.py` file setup :)

* You have a `requirements.txt` file in your project directory, with `fastapi` listed

* You have followed the instructions in [VS Code's Python FastAPI guide](https://code.visualstudio.com/docs/python/tutorial-fastapi) to:
    * Create a virtutal environment
    * Select the correct Python interpreter
    * Install the required dependencies


To start your API, run the following command:

```bash
uvicorn main:app --reload
```
---

*God speed.*