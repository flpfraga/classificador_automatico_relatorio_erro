import nltk
"""
Created on Wed Jun 26 16:10:58 2019

@author: Felipe Fraga
"""

def funcao_tokenize (texto):
    palavras = nltk.word_tokenize(texto)
    return palavras

def funcao_listar_palavras (lista_problemas): #função que recebe a lsitagem dos relatorios de erros e representa esse texto no formato saco de palavras
    aux_problema = ''
    lista_palavras = []
    
    for problema in lista_problemas: 
        aux = problema.split(';')
        
        if aux[0] == '':
            break
        
        aux_problema+=aux[0]+' '
        
    tokem_palavra_problema = funcao_tokenize(aux_problema)
    
    while len(tokem_palavra_problema)>0:
        aux_palavra = tokem_palavra_problema[0]
        lista_palavras.append(aux_palavra)
        del(tokem_palavra_problema[0])
        
        while aux_palavra in tokem_palavra_problema:
            indice = tokem_palavra_problema.index(aux_palavra)
            del(tokem_palavra_problema[indice])
            
    return lista_palavras

def funcao_palavras_relevantes(saco_de_palavras, lista_problemas): #funçao que calcula valores de acordo com o método X2-estatística
    resultado = []
    
    for palavra in saco_de_palavras:
        A = 0
        B = 0
        C = 0
        D = 0
        
        for problema in lista_problemas:
            aux_problema = problema.split(';')
            tokem_problema = funcao_tokenize(aux_problema[0])
            
            if (palavra in tokem_problema):
                
                if aux_problema[1] =='1':
                    A+=1
                    
                else:
                    B+=1
            else:
                
                if aux_problema[1] == '1':
                    C+=1
                    
                else:
                    D+=1
                    
        aux_resultado = palavra+';'+str(A)+';'+str(B)+';'+str(C)+';'+str(D)
        resultado.append(aux_resultado)
        
    return resultado

lista_P = [] #variável que vai armazenar os problemas a serem utilizados na mineração
arq = open ('arquivos/lista_P.csv', 'r')

for linha in arq:
    lista_P.append(linha)

arq.close()

saco_de_palavras = funcao_listar_palavras (lista_P)#representa o texto no formato saco de palavras
saco_de_palavras.sort() #ordena os termos por ordem alfabética
aux = '' 
arq = open ('arquivos/saco_de_palavras.csv','w')#cria o arquivo saco de palavras
for linha in lista_palavras:
    arq.writelines(linha+'\n')
    aux += linha+', '
arq.close()

lista_AC = []
arq = open ('arquivos/lista_AC.csv', 'r')
for linha in arq:
    lista_AC.append(linha)

arq.close()


indice_importancia = funcao_palavras_relevantes(saco_de_palavras, lista_P) #calcula o valor de A, B, C e D

arq = open ('arquivos/lista_I.csv', 'w')# cria um arquivo com os valores de A, B, C e D, de acordo com a aparição das palavras. O índice foi calculado por forma do excel
for linha in indice_importancia:
    arq.writelines(linha+'\n')
arq.close()