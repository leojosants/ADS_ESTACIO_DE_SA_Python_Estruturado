"""
    Suponha que, durante a execução, o usuário entre com a palavra “numero” quando solicitado. Assinale a opção que mostra o resultado imediato desta ação.
"""
try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")
