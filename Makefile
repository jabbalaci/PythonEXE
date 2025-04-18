cat:
	cat Makefile

exe:
	pyinstaller --onefile hello.py

exe2:
	pyinstaller --onefile --noupx hello.py
