def saludar():
    print('Hola mundo')

def saludar_con_parametro(nombre):
    print(f'Hola como estas {nombre}')

if __name__ == '__main__':
    saludar()
    saludar_con_parametro('Luis')