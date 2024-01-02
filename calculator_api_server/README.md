# Calculator API Server

## Tech Stack

- FastAPI
- Uvicorn

## How to Run

1. Clone this repository and change directory to this project
    ```shell
    git clone https://github.com/eunnbi/zero-to-hero.git
    cd calculator_api_server
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