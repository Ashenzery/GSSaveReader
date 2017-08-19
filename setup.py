from cx_Freeze import setup, Executable

setup(
    name = "GSSaveReader",   #Name of exe file
    version = "0.0.0.1", 
    description = u"Удобное отображение вещей на персонажах",
    executables = [Executable("main.py")]
)