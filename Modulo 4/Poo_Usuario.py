#Creacion de la clase
class Usuario():
    #Declaracion de atributos
    nombre = "Angel"
    edad = 47
    login = "admin"
    password = "1234"
    email = "angel@prueba.com"
    telefono = 666666666

    #Declaracion de metodos
    def resumen(self): #self hace referencia a la instancia de clase.
        print(f'Los datos del usuario son:\n'
        f'Nombre: {self.nombre}\n'
        f'Edad: {self.edad}\n'
        f'Login: {self.login}\n'
        f'Password: {self.password}\n'        
        f'Email: {self.email}\n'
        f'Telefono: {self.telefono}')
    
    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce edad entre 18 - 100: "))
        if(18 < edadIntroducida < 100 ):
            self.edad = edadIntroducida
            print("Edad introducida correcta")
            return ""
        else:
            print("Edad introducida No es correcta")
            self.cambiaEdad()
            return ""
    
    def muestraEdad(self):
        print("La edad del usuario es de:", self.edad, "años.")
        return ""
    
#Creacion de una instancia de la clase Usuario a la que llamaremos administrador
administrador = Usuario()

#Una vez creado el objeto administrador, hacemos uso del método resumen()
#perteneciente a la clase Usuario
administrador.resumen()

#Usamos los metodos cambiaEdad() y muestraEdad() de la clase Usuario.
print(administrador.cambiaEdad())
print(administrador.muestraEdad())

              