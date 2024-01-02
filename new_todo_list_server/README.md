# Todo List Server

todo list web application server

> Create todo, Read todos, Update todo, Delete todo

## Tech Stack
- FastAPI
- Uvicorn
- Poetry
- SQLite

## How to Run

1. Clone this repository and change directory to this project
    ```shell
    git clone https://github.com/eunnbi/zero-to-hero.git
    cd new_todo_list_server
    ```
2. Install the dependencies using poetry (You need to install `poetry` in advance)
   ```shell
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
