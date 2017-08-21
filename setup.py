# encoding: utf-8


from cx_Freeze import setup, Executable

setup(
    name = 'GSSaveReader',   #Name of exe file
    version = "1.0.0.0",
    description = u'Удобный просмотр ваших сохранений',
    executables = [Executable('main.py')]
)
