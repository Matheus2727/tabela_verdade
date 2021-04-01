import importlib
import os

print("Exemplo de funcionamento: ")
print('Ao escolher "numero de variaveis" = 2 e "expressao" = "A.(A+B)" teremos como output a exposição dessa expressao em portas logicas e sua tabela verdade.')
print('No caso "a and ( a or b )" e "[0, 0, 1, 1]" respectivamente.')
print('Sempre coloque a expressao entre "".')
print("As letras estarão disponíveis dependendo da quantidade de variáveis que você irá inserir.")
print("Por exemplo, para utilizar a letra 'b', é preciso indicar que serão utilizadas pelo menos 2 variáveis, para 'c' pelo menos 3 e assim por diante.")
print("O minimo de variaveis é 2 e o maximo é 4.")
print("Maiusculos e minusculos tem o mesmo valor. também podem ser usados os simbolos: [+], [.], [*], [(], [)], ['], [^].")
print("")
            
def iniciar():  # determina qual caso sera rodado dentro de 'rodar.py'
    global numero
    numero = int(input("quantas variaveis vai usar? "))

def import_inicial():  # primeira importação de 'rodar.py' pra evitar problemas com a importlib e com a ausencia do arquivo
    global rodar
    try:
        import rodar
        
    except:
        arq = open("rodar.py", "w")
        arq.close()
        import rodar
    
def traduzir():  # transforma o input (o qual esta em simbolos) para a logica aceita no python (em formato string) pra ser executado posteriormente
    global tradu_str
    local = []
    expressao = input("qual a expressao? ").lower()
    letras = ["a", "b", "c", "d"]
    tradu = []
    tradu_str = ""
    for i, l in enumerate(expressao):
        contador = 0
        if contador == 0:
            if i < len(expressao)-1:
                if (expressao[i+1] == "'" or expressao[i+1] == "’") and l in letras:
                    contador = 1
                    tradu.append(" not({})".format(l))
                    
        if contador == 0 and (l != "'" and l != "’"):
            if l == " ":
                pass
            
            if l == '"':
                pass
            
            elif l == "." or l == "*":
                tradu.append(" and")
                
            elif l == "+":
                tradu.append(" or")
                
            elif l == "^":
                tradu.append(" ^")
                
            elif l == "(":  
                local.append(len(tradu))
                tradu.append(" (")
                
            elif l == ")":  # ao fechar o parentese, todo o conteudo ate o ultimo parentese aberto é encarado como um grupo
                if i < len(expressao)-1:
                    if expressao[i+1] == "'" or expressao[i+1] == "’":  # testando se o grupo recebe a influencia de uma porta not
                        contador = 1
                        tradu = tradu[:local[len(local)-1]] + [" not"] + tradu[local[len(local)-1]:]
                        
                    local.pop(len(local)-1)  # retirando o grupo da lista de indices
                    
                tradu.append(" )")
                
            else:
                tradu.append(" {}".format(l))
                
        else:
            contador = 0

    for palavra in tradu:
        tradu_str += palavra

    print(tradu_str[1:])

def recarregar():  # importa uma nova versao do 'rodar.py' respeitando as alteraçoes feitas anteriormente e executa sua função principal
    a = importlib.reload(rodar)
    a.rodar()

def escrita():  # apaga o conteudo do 'rodar.py' e o refaz com as informaçoes obtidas nas outras funçoes
    arq = open("rodar.py", "w")
    arq.write("global bi\n")
    arq.write("global lista\n")
    arq.write("\n")
    arq.write("bi = [0, 1]\n")
    arq.write("lista = []\n")
    arq.write("numero = {}\n".format(numero))
    arq.write("\n")
    arq.write("def rodar():\n")
    arq.write("    for a in bi:\n")
    arq.write("        for b in bi:\n")
    arq.write("            if numero == 2:\n")
    arq.write("                 lista.append({})\n".format(tradu_str))
    arq.write("            for c in bi:\n")
    arq.write("                if numero == 3:\n")
    arq.write("                    lista.append({})\n".format(tradu_str))
    arq.write("                for d in bi:\n")
    arq.write("                    if numero == 4:\n")
    arq.write("                        lista.append({})\n".format(tradu_str))
    arq.write("\n")
    arq.write("    lista1 = []\n")
    arq.write("    for a in lista:\n")
    arq.write("        if a == True:\n")
    arq.write("            lista1.append(1)\n")
    arq.write("        elif a == False:\n")
    arq.write("            lista1.append(0)\n")
    arq.write("        else:\n")
    arq.write("            lista1.append(a)\n")
    arq.write("    print(lista1)")
    arq.close()

    recarregar()

def main():  # roda as funçoes na ordem desejada
    import_inicial()
    iniciar()
    while True:
        traduzir()
        escrita()
        print("")

if __name__ == "__main__":
    main()


