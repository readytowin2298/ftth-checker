@ECHO OFF
echo hi Tim!
echo %~dp0
IF NOT EXIST "%~dp0\venv\scripts\activate.bat" (
    python -m venv venv
    venv\scripts\activate.bat
    pip install -r requirements.txt
    python test_app.py
    echo ==============================================
    echo HHII TIM!
    echo please exit the virtual environment before closing terminal
    echo enter command "deactivate"
    echo failing to do so can cause issues during later use, if in doubt delete /venv and /__pycache__
    echo ==============================================
    cmd /k
) ELSE (
    venv\scripts\activate.bat
    pip install -r requirements.txt
    python test_app.py
    echo ==============================================
    echo HHII TIM!
    echo please exit the virtual environment before closing terminal
    echo enter command "deactivate"
    echo failing to do so can cause issues during later use, if in doubt delete /venv and /__pycache__
    echo ==============================================
    cmd /k
)
