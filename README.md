# Web Server

Flask python server to download files from server.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies.
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Place your desired file to install in the root directory of the project, it must be a ".pdf" or ".epub" file and there must be only one file of any of these types.

### Method 1: Run File
2. Run the `app.py` file.
    ```bash
    python app.py
    ```
    This will start the application on `localhost` and port `5001`.
2. Open your web browser and navigate to `<host>:<port>` to download the file. By default, navigate to `localhost:5001`.

### Method 2: Flask Command - Setup Host and Port manually
2. Start the application on your desired host and port.
    ```bash
    flask run --host=<host> --port=<port>
    ```
    For example, to start the application on `localhost` and port `5001` 
    ```bash
    flask run --host=0.0.0.0 --port=5001
    ```
3. Open your web browser and navigate to `<host>:<port>` to download the file.


## TODO

- Create landing page with all files within directory "files" of the server and serve all files within the directory in a list format.