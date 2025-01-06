# Weight Logger Application

## Overview
The Weight Logger application is a simple GUI-based tool built with Python and Tkinter that allows users to log their weight and view their weight history. The application stores weight entries in a JSON file for easy access and management.

## Project Structure
```
weight-logger-app
├── venv                # Virtual environment containing dependencies
├── src                 # Source code for the application
│   ├── weight_logger.py # Main application code
│   └── requirements.txt  # Required Python packages
├── logs                # Directory for log files
│   └── weight_log.json  # JSON file storing weight log data
├── setup.bat          # Batch file to set up and run the application
└── README.md          # Documentation for the project
```

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd weight-logger-app
   ```

2. **Create and Activate the Virtual Environment**
   - On Windows:
     ```
     venv\Scripts\activate
     ```

3. **Install Dependencies**
   ```
   pip install -r src/requirements.txt
   ```

4. **Run the Application**
   - You can run the application by executing the `setup.bat` file, which will activate the virtual environment and start the application:
     ```
     setup.bat
     ```

## Usage
- Open the application, and you will see fields to enter your weight and view the current date and log status.
- Enter your weight in kilograms and click "Save" to log it.
- Click "Display" to view your weight history in a graphical format.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.