def cuadrado(num1) :
    return num1*num1
def rectangulo(num1,num2) :
    return num1*num2
def triangulo(num1,num2) :
    return (num1*num2)/2
def trapecio(num1,num2,num3) :
    return ((num1+num2)*num3)/2

while True: 
    print("Calculadora del area de distintas figuras")
    print("Elija una de las siguientes opciones")
    print("a) Cuadrado")
    print("b) Rectangulo")
    print("c) Triangulo")
    print("d) Trapecio")
    print("e) Salir")
    
    opcion=input("Ingrese la opcion (a,b,c,d,e): ")
    
    if opcion in ["a"]:
        num1=float(input("Ingresa la medida de uno de los lados en centimetros: "))
        
        if opcion=="a":
            resultado=cuadrado(num1)
            print("El resultado del area de tu cuadrado es de: ", resultado, "centimetros cuadrados")
            
    if opcion in ["b","c"]:
        num1=float(input("Ingresa la medida de la base en centimetros: "))
        num2=float(input("Ingresa la medida de la altura en centimetros: "))
        
        if opcion=="b":
            resultado=rectangulo(num1,num2)
            print("El resultado del area de tu rectangulo es de: ", resultado, "centimetros cuadrados")
        elif opcion=="c":
            resultado=triangulo(num1,num2)
            print("El resultado del area de tu triangulo es de: ", resultado, "centimetros cuadrados")
    
    if opcion in ["d"]:
        num1=float(input("Ingresa la medida de la base superior en centimetros: "))
        num2=float(input("Ingresa la medida de la base inferior en centimetros: "))
        num3=float(input("Ingresa la medida de la altura en centimetros: "))
        
        if opcion=="d":
            resultado=trapecio(num1,num2,num3)
            print("El resultado del area de tu trapecio es de: ", resultado, "centimetros cuadrados")
    
    elif opcion=="e":
        print("Cerrando el programa. . .")
        break
    
    else:
        print("Opcion invalida")
        
    input("Presiona Enter para continuar. . .")