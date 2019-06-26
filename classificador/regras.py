import nltk
"""
Created on Wed Jun 26 17:16:17 2019

@author: Felipe Fraga
"""
def funcao_tokenize (texto): #função que cria uma lista transformando cada elemento de uma String em um elemento da lista
    palavras = nltk.word_tokenize(texto)
    return palavras

def funcao_conjunto_regras(lista_importancia, lista_AC): #funcao que verifica aparição de termos de importancia nos relatorios
    palavras_conjunto_regras = []
    
    for problema in lista_AC:
        tokem_problema = funcao_tokenize(problema)
        aux_palavras_conjunto_regras = ''
            
        for palavra in lista_importancia:
            
            if palavra in tokem_problema:
                aux_palavras_conjunto_regras+= palavra+';'
                
        palavras_conjunto_regras.append(aux_palavras_conjunto_regras)
        
    return palavras_conjunto_regras


lista_AC = [] #cria lista de problemas AC a partir de arquivo já salvo
arq = open ('arquivos/lista_AC.csv', 'r')
for linha in arq:
    lista_AC.append(linha)

arq.close()


lista_maior_importancia = [] #lista a ser criada a partir do saco de palavras com maior índice de importância
arq = open ('arquivos/lista_maior_importancia.csv', 'r')

for linha in arq:
    aux = linha.split(';')
    
    if (aux[0]==''):
        break
    
    lista_maior_importancia.append(aux[0].replace('\n', ''))

arq.close()

lista_menor_importancia = []#lista a ser criada a partir do saco de palavras com menor índice de importância
arq = open ('arquivos/lista_menor_importancia.csv', 'r')

for linha in arq:
    aux = linha.split(';')
    
    if (aux[0]==''):
        break
    
    lista_menor_importancia.append(aux[0].replace('\n', ''))

arq.close()


lista_regras_A = funcao_conjunto_regras(lista_maior_importancia, lista_AC) #cria regras a partir da aparição dos termos de maior importância nos relatorios de erros

arq = open ('arquivos/lista_regras_A.csv', 'w') #cria conjunto de regras das aparições das palavras em problemas ac

for linha in lista_regras_A:
    arq.writelines(linha+'\n')

arq.close()

lista_regras_B = funcao_conjunto_regras(lista_menor_importancia, lista_AC)#cria regras a partir da aparição dos termos de menor importância nos relatorios de erros
print (lista_regras_B)
arq = open ('arquivos/lista_regras_B.csv', 'w') #cria conjunto de regras das aparições das palavras em problemas ac

for linha in lista_regras_B:
    arq.writelines(linha+'\n')

arq.close()

lista_outros = [] #cria lista de problemas não AC a partir de arquivo já salvo
arq = open ('arquivos/lista_outros.csv', 'r')

for linha in arq:
    lista_outros.append(linha)

arq.close()

lista_nao_regras_A = funcao_conjunto_regras(lista_maior_importancia, lista_outros) #cria regras a partir da aparição dos termos de maior importância nos relatorios de erros

arq = open ('arquivos/lista_nao_regras_A.csv', 'w') #cria conjunto de regras das aparições das palavras em problemas ac

for linha in lista_nao_regras_A:
    arq.writelines(linha+'\n')

arq.close()

lista_nao_regras_B = funcao_conjunto_regras(lista_menor_importancia, lista_outros)#cria regras a partir da aparição dos termos de menor importância nos relatorios de erros

arq = open ('arquivos/lista_nao_regras_B.csv', 'w') #cria conjunto de regras das aparições das palavras em problemas ac

for linha in lista_nao_regras_B:
    arq.writelines(linha+'\n')

arq.close()