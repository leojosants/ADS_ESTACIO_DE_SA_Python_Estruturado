def func1():
    global x
    x = 10  #   variável global para a função e local para o programa principal
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20  #   variável global para a função e local para o programa principal
    print(f'Função func2 - x = {x}')


x = 0   #   variável global para para o programa principal e local para a função
func1()
func2()
print(f'Programa principal - x = {x}')
