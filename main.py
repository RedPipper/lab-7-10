from console import consola

app = consola()
app.__init__()
methods = [func for func in dir(app) if func.find('_')]

while True:
    print("Comenzile posibile sunt: ")
    for i, method in enumerate(methods):
        print(str(i+1) +'.'+ method)
    
    choice = input("introdu comanda aleasa: ")
    result = getattr(app, choice)
    print('\n'*2)
    result()
    print('\n'*2)

