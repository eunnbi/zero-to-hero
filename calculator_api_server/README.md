# Calculator API Server

## Tech Stack

- FastAPI
- Uvicorn

## How to Run

1. Clone this repository and change directory to this project
    ```shell
    git clone https://github.com/eunnbi/zero-to-hero.git
    cd zero-to-hero/calculator_api_server
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