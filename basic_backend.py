import mvc_exceptions as mvc_exc

items = list()

def create_item(name, priority, author, description, owner='none', state='open', result='open'):
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
    else:
        items.append({'name': name, 'priority': priority, 'owner': owner, 'author': author, 'description': description, 'state': state, 'result': result})

def create_items(app_items):
    global items
    items = app_items

def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(name))

def read_items():
    global items
    return [item for item in items]

def update_item(name, priority, author, description, owner='none', state='open', result='open'):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'priority': priority, 'owner': owner, 'author': author, 'description': description, 'state': state, 'result': result}
    else:
        raise mvc_exc.ItemNotStored('Can\'t update "{}" because it\'s not stored'.format(name))
    
def delete_item(name):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored('Can\'t delete "{}" because it\'s not stored'.format(name))


# test them
def main():
    my_items = [
            {'name': 'tlacitko', 'priority': 3, 'owner': 'none', 'author': 'Michal', 'description': 'blech', 'state': 'open', 'result': 'result'},
            {'name': 'ledka', 'priority': 1, 'author': 'Michal', 'description': 'description', 'state': 'open', 'result': 'result'},
            {'name': 'blikani', 'priority': 2, 'author': 'Standa', 'description': 'description', 'state': 'open'}
        ]

    # CREATE
    create_items(my_items)
    create_item('semaphore', priority=2, author='Michal', description='Neblika')
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('READ items')
    print(read_items())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chyba')
    # print(read_item('chyba'))

    # UPDATE
    print('UPDATE tlacitko')
    update_item('tlacitko', priority=2, author='Michal', description='Neblika')
    print(read_item('tlacitko'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chyba')
    # update_item('chyba', priority=2, author='Michal', description='Nechybi')

    # DELETE
    print('DELETE ledka')
    delete_item('ledka')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chyba')
    # delete_item('chyba')

    print('READ items')
    print(read_items())

if __name__ == '__main__':
    main()