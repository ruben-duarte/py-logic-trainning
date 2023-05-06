primer_digito = input("Digite un número entre 0 y 9 :  ")
primer_digito = int(primer_digito)

for  n in range(10):
    
    seguir = input(" 1 seguir, 2 detener :  ")
    if seguir == 1:
        print(str(n) + " +  " + str(primer_digito) + " = ")
    print(str(n) + " +  " + str(primer_digito) + " = ")
    suma = primer_digito + n
    print(suma)

    
    



    
          

    



    


    
