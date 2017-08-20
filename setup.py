from cx_Freeze import setup, Executable

setup(
    name = 'GSSaveReader',   #Name of exe file
    version = "0.0.0.5",
    description = u'Удобный просмотр ваших сохранений',
    executables = [Executable('main.py')]
)
