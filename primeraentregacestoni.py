
#definicion de diccionario
usuarios={}
#variable para mantener el programa activado
programaprendido=1 

#pregunta de continuidad en el programa
def pregunta():
    opcionsino=int(input("Desa continuar --1.Sí -- 2.No : " ))
    if opcionsino==1:
            True
    elif opcionsino==2:
        print("programa cerrado")
        global programaprendido

        programaprendido=0
    else:
        print("Opcion inválida")
        pregunta()
        
#funcion para crear cuenta 
def crearcuenta():
    print("Crar Cuenta")
    usuario = str(input("ingrese usuario: "))
    usuario=usuario.lower()
    if usuario in usuarios:
     
   
        print("El usuario ya existe")
    else: 
        contrasena = str(input("ingrese contraseña: "))
        contrasena=contrasena.lower()
        usuarios[usuario]= contrasena
        print(f"Usuario {usuario} creado con éxito!")

#funcion para ingresar
def ingresar():

    print("Ingresar")
    usuario = str(input("ingrese usuario: "))
    usuario= usuario.lower()
    contrasena = str(input("ingrese contraseña: "))
    contrasena=contrasena.lower()

    if usuario in usuarios:  
        if usuarios[usuario]== contrasena:
            print("Ingresó correctamente")
            
        else: 
            print("Contraseña incorrecta")
            
    else:         
        print("Usuario incorrecto")
#funcion para cambiar contraseña   
def modificarcont():
    usuario=str(input("Ingrese usuario a modificar: "))
    usuario=usuario.lower()
    if usuario in usuarios:
        contrasenacamb=str(input("Ingrese la contgraseña a cambiar: "))
        contrasenacamb=contrasenacamb.lower()
        usuarios[usuario]=contrasenacamb
        print("contraseña cambiada correctamente")
    else:
        print("el usuario no existe")

#funcion para ver los usuarios creados       
def listausuario():
        print("Lista de usuarios")
        contador=1
        for usuario in usuarios:
            
             print(f"{contador} - {usuario}")
             contador=contador+1
#funcion del menu            
def menu():
    global programaprendido
    while programaprendido==1:
   
        print("Bienvenido al Login")
        print("1.Crear Cuenta")
        print("2.Ingresar")
        print ("3.Modificar Contraseña")
        print ("4.Lista de Usuarios")
        print ("5.Salir")
        
        valoropcion=int(input("Ingrese una opcion:" ))
        #verificaciones de opcion seleccionada
        if valoropcion==1:
            crearcuenta()
            pregunta()
            
        elif valoropcion==2:
            ingresar()
            pregunta()
            
        elif valoropcion==3:
            modificarcont()
            pregunta()
           
        elif valoropcion==4:
            listausuario()
            pregunta()
            
        elif valoropcion==5:
            print("programa cerrado")
            programaprendido=0
        else:
            print("Opcion invalida")
            pregunta()
#ejecución del programa
menu()            

    