# CALCULADORA

from calculadora.operaciones import suma, resta, multiplicacion, division, potencia, division_entera

def main():
    print("Bienvenido a la calculadora modular")
    
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        operador = input("Introduce el operador (+, -, *, /, **, //): ")

        if operador == '+':
            resultado = suma(num1, num2)
        elif operador == '-':
            resultado = resta(num1, num2)
        elif operador == '*':
            resultado = multiplicacion(num1, num2)
        elif operador == '/':
            resultado = division(num1, num2)
        elif operador == '**':
            resultado = potencia(num1, num2)
        elif operador == '//':
            resultado = division_entera(num1, num2)
        else:
            raise ValueError("Operador inválido.")

        print(f"El resultado de {num1} {operador} {num2} es: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
