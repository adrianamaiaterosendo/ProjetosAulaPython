#escrever use o 'w' e alterar use o 'a'
def escrever_arquivo(texto):
    arquivo = open("teste.txt", "a")
    arquivo.write('\nTerceira escrita')
    arquivo.close()

def atualizar_arquivo(testo):
    arquivo = open('teste.txt')
    arquivo.write(texto)
    arquivo.close()

if __name__ == '__main__'
