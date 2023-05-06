primer_digito = input("Digite un número entre 0 y 9 :  ")
primer_digito = int(primer_digito)

import random

for  n in range(20):
    r = random.randint(0,9)
    suma = primer_digito + r
    seguir = input(" 1 seguir, 2 detener :  ")
    print(str(primer_digito) + " +  " + str(r) + " =                                                                                                            ",suma)

    

