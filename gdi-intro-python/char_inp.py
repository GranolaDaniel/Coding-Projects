from datetime import *

name = input('Hello! What\s your name? ')
age = input('And how old are you? ')

birth_year = age - int(strftime('%Y'))
