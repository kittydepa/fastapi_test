# A Simple Foraging API

Making a simple API with FastAPI and **uvicorn**.
The main purpose is to try out FastAPI + documentation generation (with Redoc).

Another purpose of this project is to learn basic usage of FastAPI, by following the core **CRUD** pattern:

* <ins>C</ins>reate with `POST`

* <ins>R</ins>ead with `GET`

* <ins>U</ins>pdate with `PUT`

* <ins>D</ins>elete with`DELETE`

This API will be a simple foraging log, including information about mushrooms and berries you can forage in Sweden.

# Setup

Before you start, make sure you have the proper setup (especially if using VS Code with FastAPI), which includes:

* You have installed `fastapi` and `uvicorn`

* You have a `main.py` file setup :)

* You have a `requirements.txt` file in your project directory, with `fastapi` listed

* You have followed the instructions in [VS Code's Python FastAPI guide](https://code.visualstudio.com/docs/python/tutorial-fastapi) to:
    * Create a virtual environment
    * Select the correct Python interpreter
    * Install the required dependencies

---

**Tip:** To start your API, run the following command:

```bash
uvicorn main:app --reload
```

See [Step-by-step instructions](./steps.md) for detailed instructions.

---

*Godspeed.*


