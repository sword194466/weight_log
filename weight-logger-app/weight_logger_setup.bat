@echo off
REM Activate the virtual environment
call venv\Scripts\activate

REM Run the weight_logger.py script
python src\weight_logger.py

REM Pause the command window to see any messages
pause