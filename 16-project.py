import os

FILE = 'contacts/' 
EXTENSION = '.txt'


class Contact:
    def __init__(self, name, phone, category):
        self.name = name
        self.phone = phone 
        self.category = category 


def app():
    create_directory()
    show_menu()

    ask = True
    while ask:
        option = input('Seleccione una opción: \r\n')
        option = int(option)

        if option == 1:
            create_contact()
            ask = False
        elif option == 2:
            edit_contact()
            ask = False
        elif option == 3:
            print('ver')
            ask = False
        elif option == 4: 
            print('buscar')
            ask = False
        elif option == 5: 
            print('eliminar')
            ask = False
        else:
            print('Opción incorrecta, inténtelo de nuevo')

def create_contact():
    print('Introduzca los datos:')
    name_contact = input('Nombre: \r\n')

    #revisar si contacto ya existe
    exists = existing_contact(name_contact)    
    if not exists:   
        phone_contact = input('Teléfono: \r\n')
        category_contact = input('Categoria: \r\n') 
        
        with open(FILE + name_contact + EXTENSION, 'w') as file:
            contact = Contact(name_contact, phone_contact, category_contact) #instanciar la clase
            write_file(contact, file) #editar archivo
            print('Contacto creado correctamente')
    else:
        print('ya existe un archivo con ese nombre')
        #reiniciar app
        app()

def edit_contact():
    existing_name = input( 'Nombre del contacto que desea editar: \r\n')
    exists = existing_contact(existing_name)
    if exists:
        with open(FILE + existing_name + EXTENSION, 'w') as file:
            name_contact = input ('Edita nombre: \r\n')
            phone_contact = input('Edita teléfono: \r\n')
            category_contact = input('Edita categoria: \r\n')

            contact = Contact(name_contact, phone_contact, category_contact)
            write_file(contact, file)
            print('editado correctamente')

            #rename file
            os.rename(FILE + existing_name + EXTENSION, FILE + name_contact + EXTENSION )
    else:
        print('contacto no encontrado, inténtelo de nuevo o cree uno')
        app()#reiniciar app


  
def create_directory():
    if not os.path.exists('contacts/'):
        #create file
        os.makedirs('contacts/')
     
def show_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def existing_contact(name_contact):
    exists = os.path.isfile(FILE + name_contact + EXTENSION)
    if exists:
        return True 

def write_file(contact, file):
#escribir archivo
    file.write('Nombre: '+ contact.name+ '\r\n')
    file.write('Telefono: ' + contact.phone+ '\r\n')
    file.write('Categoría: ' + contact.category + '\r\n')



app()