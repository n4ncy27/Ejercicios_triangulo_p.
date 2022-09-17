# determinar si es un triangulo es obtuso,recto o agudo

print ( "----------------------------------------" )
print ( "-----triangulo obtuso,recto o agudo-----" )
print ( "----------------------------------------" ) 
imprimir ( "-------------------------------------" )
  
#aporte
a = int ( input ( "dijite el valor del angulo a" ))
b = int ( input ( "dijite el valor del angulo b" ))
c = int ( input ( "dijite el valor del angulo c" ))

#Procesando
if ( a + b + c == 180 ):
    if ( 0 < a <= 90 ) and ( 0 < b <= 90 ) and ( 0 < c <= 90 ):
        print ( "si es un triangulo agudo" )
    else:
        print ( "no es un triangulo agudo" )   
    if ( 90 < a <= 180  and  b <= 90  and  c <= 90 ) or ( 90 < b <= 180  and  a <= 90  and  c <= 90 ) or ( 90 < c <= 180  and  a <= 90  and b  <= 90 ):
        print ( "si es un triangulo obtuso" )
    else:
        print ( "no es un triangulo obtuso" )  
    if ( a == 90  or  b == 90  or  c == 90 ):
        print ( "si es un triangulo recto" )
    else:
        print ( "no es un triangulo recto" )
else:
    print ( "no es triangulo porque la suma de sus angulos internos no es 180" )


# FIN