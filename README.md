# Web Server

Simple web server to serve files from a directory. Made using Flask.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies.
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Place your desired files to be served in the `/Books` directory.

### Method 1: Run File
2. Run the `app.py` file.
    ```bash
    python app.py
    ```
    This will start the application on `localhost` and port `5001` (To navigate to the application, on other devices, use the IP address of the device running the application).


### Method 2: Flask Command - Setup Host and Port manually
2. Start the application on your desired host and port.
    ```bash
    flask run --host=<host> --port=<port>
    ```
    For example, to start the application on `localhost` and port `5001` 
    ```bash
    flask run --host=0.0.0.0 --port=5001
    ```

4. Open your web browser and navigate to `<host>:<port>` to obtain a list of all the files in the `/Books`.

5. Click on the filename of the file to download the file.