class agenda():
    def __init__(self):
        self.contactos=[]
    def añadir(self):
        Nombre=input("Digite el nombre")
        Telefono=int(input("Digite el número de telefono"))
        while len(str(Telefono))!=10:
            Telefono=int(input("Digite el número de telefono correctamente"))
        while True:
            correo = input("Digite el correo electrónico: ")
            if "@" in correo:
                break
            else: print("Digite correctamente el correo electrónico.")
        self.contactos.append({"Nombre":Nombre,"Telefono":Telefono,"correo":correo})
        print("usuario registrado")
        self.menu()
        
    def Buscar(self):
        name=input("contacto que desea buscar")
        for contacto in self.contactos:
            if contacto["Nombre"]==name:
                print("Nombre: ", contacto["Nombre"])
                print("Telefono: ", contacto["Telefono"])
                print("Correo: ", contacto["correo"])
            else :print("El nombre del usuario que busca no esta")
        self.menu()
    def lista(self):
        print("Nombre\t","Telefono\t ","correo\t")
        for contacto in self.contactos:
            print(contacto["Nombre"],"\t",contacto["Telefono"],"\t",contacto["correo"])
        self.menu()
    def Editar(self):
        name=input("Digite el nombre del contacto que desea editar O en caso de no editar escriba(salir ) para volver al menu ")
        if name=="salir":
            self.menu()
        for contacto in self.contactos:
            if contacto["Nombre"]==name:
                print(''' ¿Que desea editar?
                    1.Nombre
                    2.Telefono
                    3.Correo''')
                edi=int(input("Digite una opcion"))
                if edi==1:
                    nuenombre=input("Digite el nuevo ")
                    contacto["Nombre"]=nuenombre
                    print("Contacto editado")
                    self.Editar()
                elif edi==2:
                    nuetelefono=input("ingrese el nuevo numero de telefono")
                    while len(str(nuetelefono))!=10:
                        nuetelefono=int(input("Digite el número de telefono correctamente"))
                    contacto["Telefono"]=nuetelefono
                    print("Numero de telefono editado")
                    self.Editar()
                elif edi==3:
                    corr=input("ingrese el correo :")
                    while True:
                        if "@" in corr:
                            break
                        else:input("Ingrese el correo correctamente  ")
                    contacto["correo"]=corr
                    print("Correo editado")
                    self.Editar()
    def Eliminar(self):
        borrar=input("ingrese el nombre del contacto que desea eliminar  ")
        for contacto in self.contactos:
            if contacto["Nombre"]==borrar:
                self.contactos.remove(contacto)
                print("contacto eliminado")
            else:
                print("el contacto no existe")
                self.Eliminar()
        self.menu()      
    def menu(self):
        print('''AGENDA
                        Opciones
                        1.Añadir
                        2.Buscar
                        3.Lista
                        4.Editar 
                        5.Eliminar''')
        op=int(input("Digite la opcion"))
        if op==1:
            self.añadir()
        elif op==2:
            self.Buscar()
        elif op==3:
            self.lista()
        elif op==4:
            self.Editar()
        elif op==5:
            self.Eliminar()
        else: 
            print("opcion invalida")
            self.menu()

agenda=agenda()
agenda.menu()