message = '150'


def isnum(value):
    if value.isnumeric():
        int(value)
        print('si se puede castear', value)
    else: 
        print('Mensjae invalido')   

isnum(message)

