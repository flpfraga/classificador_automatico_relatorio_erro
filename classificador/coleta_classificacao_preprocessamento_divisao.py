import nltk
import re
"""
Created on Wed Jun 26 15:31:29 2019

@author: Felipe Fraga
"""

def funcao_stopWord(texto): #função que retira stopwords do texto
    texto = texto.lower()
    stopwords = set(nltk.corpus.stopwords.words())
    palavras = [i for i in texto.split() if not i in stopwords]
    return (" ".join(palavras))

def funcao_re (texto): #função que retira símbolos do texto
    texto = re.sub('[-|0-9]',' ', texto)
    texto = re.sub(r'[-./<>?!,"#\'`^:;()\'~$_*@+=\[\]&\{\}%¬¨´å¯ñðº¾¸½¿ïu’‹è€˜©†âãä™ñ‚ððãâ­ç\\]',' ',texto)
    return texto

def funcao_cria_lista_problemas(arquivo, lista_ac): #funcao que le os relatórios de erros baixados no github e os organiza em uma lista, já aplicando técnicas de pré-processamento
    problemas = [] #variável que retornará os relatórios de erros organizados
    corpo = ''
    numero = ''
    cabecalho = True
    cont = 0
    for linha in arquivo:
    
        if linha == None:
            print ('Linha Vazia')#condições para leitura
        
        elif (linha.find('Total Bug' or 'Total Closed') ) >= 0: #condição de término da leitura
            break
        
        elif (linha[0] == '\"' and linha[1] == ','):
            cont+=1
            re_1 = funcao_re(corpo) #função que retira símbolos dos termos
            stopwords = funcao_stopWord(re_1) #função que retira palavras comuns
            aux = ''
                        
            if numero in lista_ac: #verifica se o relatório de erro foi classificado como AC
                aux = stopwords+';1' #marca como relatório de erro do tipo AC
                
            else:
                aux = stopwords+';0'#marca relatório de erro de outros tipos
            
            problemas.append(aux)  
            corpo = ''
            cabecalho = True
            
        elif cabecalho:
            aux = linha.split(',')
            cont1 = 0
            
            for elemento in aux:
            
                if cont1 == 0:
                    numero = elemento
                
                elif cont1 == 2:
                    aux = elemento + '; '
                    
                    
                elif cont1 > 2:
                    corpo+=elemento + '; '
                        
                cont1+=1
                cabecalho = False
                
        else:            
            corpo+=linha
            
    return problemas #retorna os problemas organizados e marcados

lista_ac =[] #variável com os número dos relatórios de erros classificados como AC
arq_2 = open('arquivos/classificacao.csv', 'r') #le o documento que contém o número dos relatórios de erros classificados como Ambiente e Configuração

for linha in arq_2:
    aux = linha.split(';')
    aux1 = aux[0]
    
    if (aux1==0):
        break
    
    lista_ac.append(aux1.replace('\n', ''))
    
arq_2.close()

lista_problemas = [] #variável com os relatórios de erros já marcados quais são AC e quais não são
arq = open ('arquivos/lista_relatorio_erros.csv', 'r') #le o arquivo bruto dos relatórios de problemas baixados do GitHub
lista_problemas = funcao_cria_lista_problemas (arq, lista_ac)
arq.close()
lista_P = [] #variável com os relatórios de erros usados na descoberta do conhecimento
lista_A = [] #variável com relatórios de erros usados na análise de eficiência do prototipo
cont_1 = 0

for linha in lista_problemas: #divisão dos relatórios de erros nas lista-P e lista-A
    
    if cont_1 <280:
        lista_P.append(linha)
        
    else:
        lista_A.append(linha)
        
    cont_1+=1
    
arq.close()
arq = open ('arquivos/lista_P.csv', 'w') #arquivo onde a lista-P é salva no sistema

for linha in lista_P: #cria o data set parte 1 final
    arq.writelines(linha+'\n')
    
arq.close()
arq = open ('arquivos/lista_A.csv', 'w')#arquivo onde a lista-A é salva no sistema

for linha in lista_A: #cria o data set parte 2 final
    arq.writelines(linha+'\n')
    
arq.close()
lista_AC = [] #lista com os problemas classificados como AC
lista_outros = [] #lista com os outros problemas

for linha in lista_P:
    aux = linha.split(';')
    
    if aux[1]=='1':
        lista_AC.append(aux[0]+'\n')
    
    else:
        lista_outros.append(aux[0]+'\n')
        
arq = open ('arquivos/lista_AC.csv', 'w') #salvando lista ac em arquivo

for linha in lista_AC:
    arq.writelines(linha)
    
arq.close()

arq = open ('arquivos/lista_outros.csv', 'w')#salvando lista outros em arquivo
for linha in lista_outros:
    arq.writelines(linha)
arq.close()
