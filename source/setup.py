import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["pygame", "random", "sys"],
                     "excludes": ['tkinter'],
                     "include_files": ['icon.ico', 'highscore.txt', 'background.bmp', 'bg_par1.bmp',
                                       'bg_par2.bmp', 'bg_par3.bmp', 'sprite_sheet.png',
                                       'Blue Space v0_96.wav', 'explosion1.wav', 'explosion2.wav', 'explosion3.wav',
                                       'powerup.wav', 'reload1.wav', 'reload2.wav', 'select.wav', 'ship_explode.wav', 'shot.wav']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
	

setup(name="Cool Asteroid Game",
      version="1.0",
      description="Shoot down asteroids",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="CoolAsteroidGame.py", base=base, icon="icon.ico")])
