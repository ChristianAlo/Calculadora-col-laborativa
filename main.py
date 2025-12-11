
from suma_resta import suma, resta
from mult_div import multiplicacio, divisio
from pot_arrel import potencia, arrel_quadrada
from percentatges import percentatge
from conversio import celsius_a_fahrenheit, fahrenheit_a_celsius
from arredonir import arredonir

def menu():
    print("\n--- CALCULADORA COL·LABORATIVA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Potència")
    print("6. Arrel quadrada")
    print("7. Percentatge")
    print("8. Conversió Celsius → Fahrenheit")
    print("9. Conversió Fahrenheit → Celsius")
    print("10. Arredonir número decimal")
    print("0. Eixir")


while True:
    menu()
    opcio = input("Tria una opció: ")
    
    if opcio == "0":
        print("Adeu!")
        break
    
    elif opcio in ["1","2","3","4","5","7"]:
        x = float(input("Introdueix el primer número: "))
        y = float(input("Introdueix el segon número: "))
    
    if opcio == "1":
        print(f"Resultat: {suma(x, y)}")
    
    elif opcio == "2":
        print(f"Resultat: {resta(x, y)}")
    
    elif opcio == "3":
        print(f"Resultat: {multiplicacio(x, y)}")
    
    elif opcio == "4":
        print(f"Resultat: {divisio(x, y)}")
    
    elif opcio == "5":
        print(f"Resultat: {potencia(x, y)}")
    
    elif opcio == "6":
        z = float(input("Introdueix el número: "))
        print(f"Resultat: {arrel_quadrada(z)}")
    
    elif opcio == "7":
        print(f"{y}% de {x} és {percentatge(x, y)}")
    
    elif opcio == "8":
        graus = float(input("Introdueix graus Celsius: "))
        print(f"{graus}°C = {celsius_a_fahrenheit(graus)}°F")
    
    elif opcio == "9":
        graus = float(input("Introdueix graus Fahrenheit: "))
        print(f"{graus}°F = {fahrenheit_a_celsius(graus)}°C")
    
    elif opcio == "10":
        numero = float(input("Introdueix el número decimal: "))
        print(f"Resultat arredonit: {arredonir(numero)}")
    
    else:
        print("Opció no vàlida.")