@echo off
rem The path to output all built .py files to: 
set UI_PYTHON_PATH=../python/app/ui

python "C:\Program Files\Shotgun\Python\bin\pyside-uic" --from-imports dialog.ui -o dialog.py
sed -i "" -e "s/from PySide import/from tank.platform.qt import/g" -e "/# Created:/d" dialog.py
move dialog.py %UI_PYTHON_PATH%

"C:\Program Files\Shotgun\Python\bin\pyside-rcc" resources.qrc > resources_rc.py
sed -i "" -e "s/from PySide import/from tank.platform.qt import/g" -e "/# Created:/d" resources_rc.py
move resources_rc.py %UI_PYTHON_PATH%

set UI_PYTHON_PATH=
