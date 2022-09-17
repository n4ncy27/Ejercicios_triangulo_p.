
# Determinar si un triangulo es equilatero, isosceles o escaleno
#Determinar si un triangulo es equilatero, isosceles o escaleno

print("------------------------------")
print("-------Lados_triangulo :------")
print("------------------------------")

# input
A = int(input("digite el primer lado del triangulo: "))
B = int(input("digite el seguno lado del triangulo: "))
C = int(input("digite el tercer lado del triangulo: "))

# proccesing
if( A + B) > C and (A + C) > B and (B + C )> A:
    print ("\n los lados corresponden a un triangulo. ")


#Equilatero = Todos los lados iguales
#Isoceles = 2 lados iguales
# Escaleno = No tiene lados iguales 

    if(A==B==C):
        print ("se trata de un triangulo Equilatero")
    elif (A==B or A==C or B==C):
        print("se trata de un triangulo Isoceles ")
    else: 
        print("se trata de un triangulo Escaleno")

# FIN