phonebook = {'nathan': {'name':'nathan', 'number': 2532980835, 'email': 'nate@gmail.com'},
             'keri': {'name': 'keri', 'number': 4253012237, 'email': 'keri@gmail.com'},
             'jared': {'name': 'jared', 'number': 1111111111, 'email': 'jatout@aol.com'},
             'natalie': {'name': 'natalie', 'number': 2222222222, 'email': 'no email'}}


def new_contact():
    name = input('Enter name: ')
    number= int(input('Enter number: '))
    email = input('Enter email: ')
    contact = {name: {'name': name,
                      'numebr': number,
                      'email': email}}
    return contact


def view_contact(pb):
    name = input('Which contact do you want to view?: ').lower()
    return pb[name]


def add_contact(pb):
    contact = new_contact()
    pb.update(contact)


def update_contact(pb):
    name = input('Which contact would you like to update?: ').lower()
    to_update = input('What info needs to be updated? (name,number,email): ').lower()
    pb[name][to_update] = input('Enter new info: ')


def remove_contact(pb):
    while True:
        name = input('Which contact would you like to remove?: ').lower()
        del_name = input('Are you sure you want to delete "{}" from the phonebook? (y/n)'.format(name.upper())).lower()
        if del_name == 'y':
            del pb[name]
        else:
            if input('Do you still want to delete a contact? (y/n): ').lower() == 'n':
                break


def search_contact(pb):
    search = input('Search for contact by name, number or email: ').lower()
    for contact in pb.values():
        for value in contact.values():
            if search in str(value):
                print(contact)


def phonebook_fun(pb):
    print('welcome to your phonebook.')
    while True:
        option = input('Would you like to "view", "add", "update", or "remove" a contact?: ')
        if option == 'view':
            search_contact(pb)
            print(view_contact(pb))
            done = input('Are you done viewing this contact? (y/n): ').lower()
            if done == 'y':
                continue
        if option == 'add':
            add_contact(pb)
            done = input('Are you done editing? (y/n): ').lower()
            if done == 'y':
                continue
        elif option == 'update':
            search_contact(pb)
            update_contact(pb)
            done = input('Are you done editing? (y/n): ').lower()
            if done == 'y':
                continue
        elif option == 'remove':
            search_contact(pb)
            remove_contact(pb)
            done = input('Are you done editing? (y/n): ').lower()
            if done == 'y':
                continue
        else:
            done = input('Look into something else? (y/n): ').lower()
            if done == 'n':
                break


phonebook_fun(phonebook)
