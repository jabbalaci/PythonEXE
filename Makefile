cat:
	cat Makefile

run:
	uv run hello.py

exe:
	uv run pyinstaller --onefile hello.py

exe2:
	uv run pyinstaller --onefile --noupx hello.py
