from enum import Enum
from typing import List
from fastapi import FastAPI, Response

app = FastAPI()

class Operations(str, Enum):
    suma = 'suma'
    resta = 'resta'
    multiplicacion = 'multiplicacion'
    division = 'division'


def math_operations(numbers, operation):
    result = numbers[0]
    if operation == 'suma':
        for i in numbers[1:]:
            result = result + i

    if operation == 'resta':
        for i in numbers[1:]:
            result = result - i

    if operation == 'multiplicacion':
        for i in numbers[1:]:
            result = result * i

    if operation == 'division':
        for i in numbers[1:]:
            if (i == 0):
                result = 'Error: Division por cero'
                break
            else:
                result = result / i

    return result


@app.post('/suma')
def suma(numbers: List[int]):
    return {'El resultado de la suma es:': math_operations(numbers, 'suma')}

@app.post('/resta')
def resta(numbers: List[int]):
    return {'El resultado de la resta es:': math_operations(numbers, 'resta')}

@app.post('/multiplicacion')
def multiplicacion(numbers: List[int]):
    return {'El resultado de la multiplicacion es:': math_operations(numbers, 'multiplicacion')}

@app.post('/division')
def division(numbers: List[int]):
    return {'El resultado de la division es:': math_operations(numbers, 'division')}

@app.post('/all_operations/{operation}')
def all_operations(operation: Operations, numbers: List[int]):
    return {f'El resultado de la {operation} es:': math_operations(numbers, operation)}



