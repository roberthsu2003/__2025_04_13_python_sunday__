from dataclasses import dataclass

PI:float = 3.1415926

def func1(a:int, b:int) -> int:
    return a + b

@dataclass
class Student:
    name:str
    chinese:int
    math:int
    english:int



