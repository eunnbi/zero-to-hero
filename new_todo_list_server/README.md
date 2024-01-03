# Todo List Server

todo list web application server

> Create todo, Read todos, Update todo, Delete todo

## Tech Stack
- FastAPI
- Uvicorn
- SQLite

## How to Run

1. Clone this repository and change directory to this project
    ```shell
    git clone https://github.com/eunnbi/zero-to-hero.git
    cd zero-to-hero/new_todo_list_server
    ```
2. Create virtual environment and install dependencies using poetry
    > You need to install `python@3.12` and `poetry` in advance
    ```shell
    poetry env use 3.12
    poetry install
    ```
3. Activate the virtual environment
   ```shell
    poetry shell
    ```
4. Run the server
    ```shell
    uvicorn app.main:app --reload
    ```