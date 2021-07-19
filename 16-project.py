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
            print('editar')
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
            print('Opción incorrecta, intente de nuevo')

def create_contact():
    print('Introduzca los datos:')
    name_contact = input('Nombre: \r\n')
    phone_contact = input('Teléfono: \r\n')
    category_contact = input('Categoria: \r\n')
    
    with open(FILE + name_contact + EXTENSION, 'w') as file:
        #instanciar la clase
        contact = Contact(name_contact, phone_contact, category_contact)

        #escribir archivo
        file.write('Nombre: '+ contact.name+ '\r\n')
        file.write('Telefono: ' + contact.phone+ '\r\n')
        file.write('Categoría: ' + contact.category + '\r\n')

     

        print('Contacto creado correctamente')

  


def show_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def create_directory():
    if not os.path.exists('contacts/'):
        #create file
        os.makedirs('contacts/')
        


app()