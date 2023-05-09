import random
print("="*50)
mensaje = """
             Practiquemos sumas con el 8

                  x 
                          +
                                  8

              🞖  🞖   🞖   🞖   🞖  🞖    🞖   🞖
"""
print(mensaje)
print("="*50)
print()
n_intentos = int(input("Ingresa el numero de intentos:  "))
print()

tablero_inicio = f"""
            
          Número de intentos:  { n_intentos }  
          la practica hace el maestro!

        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
        █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
        █░░║║║╠─║─║─║║║║║╠─░░█
        █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀       
             

    🞖  🞖   🞖   🞖   🞖  🞖    🞖   🞖
"""
print(tablero_inicio)

correcto = """

             /|~~~   
           ///|      
         /////|      
       ///////|      
     /////////|      
   \==========|===/  
~~~~~~~~~~~~~~~~~~~~~
        
                 Great!

"""

for intento in range(n_intentos):
    variable = random.randint(1,20)
    respuesta = int(input(f"{variable} +  8  =   "))
    if respuesta == 8+variable:
         print("Correcto !   :)")
         print(correcto)

         print("="*30)
         dos_antes = variable - 2
         print(f" 10  + {dos_antes}")
         print("="*30)
    else:
          print("Intenta de nuevo")
          print("""
 
                _______
               /        /,
             /        //
           /______//
          (______(/ ntenta de nuevo 

          """)
          respuesta = int(input(f"{variable} +  8  =   "))

                
