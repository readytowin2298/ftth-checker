: # This is a special script which intermixes both sh
: # and cmd code. It is written this way because it is
: # used in system() shell-outs directly in otherwise
: # portable code. See https://stackoverflow.com/questions/17510688
: # for details.
: # Linux users run chmod +x setup.cmd then run sh setup.cmd

:; echo Using Linux? I like you
:; [ ! -d "/venv" ] && python3 -m venv venv
:; alias activate=". ./venv/bin/activate"
:; activate
:; pip install -r requirements.txt
:; echo ==============================================
:; echo HHII TIM!
:; echo please exit the virtual environment before closing terminal
:; echo enter command "deactivate"
:; echo failing to do so can cause issues during later use, if in doubt delete /venv and /__pycache__
:; echo ==============================================
:; python3 test_app.py
:; deactivate
:; exit



@ECHO OFF
echo Using Windows? That's alright
echo hi Tim!
echo %~dp0
IF NOT EXIST "%~dp0\venv\scripts\activate.bat" (
    python -m venv venv
    venv\scripts\activate.bat
    pip install -r requirements.txt
    
    echo ==============================================
    echo HHII TIM!
    echo please exit the virtual environment before closing terminal
    echo enter command "deactivate"
    echo failing to do so can cause issues during later use, if in doubt delete /venv and /__pycache__
    echo ==============================================
    python test_app.py
    cmd /k
) ELSE (
    venv\scripts\activate.bat
    pip install -r requirements.txt
    
    echo ==============================================
    echo HHII TIM!
    echo please exit the virtual environment before closing terminal
    echo enter command "deactivate"
    echo failing to do so can cause issues during later use, if in doubt delete /venv and /__pycache__
    echo ==============================================
    python test_app.py
    cmd /k
)