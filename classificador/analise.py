# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:11:17 2019

@author: Felipe Fraga
"""

def problema_esta_na_arvore(arvore, problema, cont_1, caminho):#função que vai percorrendo o vetor árvore até atingir um nó folhas
    
    if cont_1 < len(arvore):
        termo = arvore[cont_1]
        caminho.append(termo)
        
        if termo =='0':
            return 0
        
        elif termo=='SIM':
            return 1
        
        else:
            
            if termo in problema:
                cont_1 = (cont_1*2)+ 1
                return problema_esta_na_arvore(arvore, problema, cont_1, caminho)
            
            else:
                cont_1 = (cont_1*2)+ 2
                return problema_esta_na_arvore(arvore, problema, cont_1, caminho)
             
    else:
        
        return 0
    
def funcao_le_arvore(nome):#le arquivos de arvores salvos
    arvore = []
    arq = open ('arquivos/'+nome+'.csv', 'r')
    
    for linha in arq:
        aux = linha.split(';')
        
        for palavra in aux:
            
            if palavra=='':
                break
            
            arvore.append(palavra)
    
    return arvore
        
    
arvore_0 = []
arvore_1 = []
arvore_2 = []
arvore_3 = []
arvore_4 = []

arvore_0 = funcao_le_arvore('arvore_1')
arvore_1 = funcao_le_arvore('arvore_2')
arvore_2 = funcao_le_arvore('arvore_3')
arvore_3 = funcao_le_arvore('arvore_4')
arvore_4 = funcao_le_arvore('arvore_5')


lista_A = []
arq = open ('arquivos/lista_A.csv', 'r')
for linha in arq:
    lista_A.append(linha)

arq.close()



caminho = []
arq = open('arquivos/acertividade.csv', 'w')#salva os relatórios e a classificação atribuida a eles pelo classificador
acuracia = 0
cont_qnt_problemas = 0
for problema in lista_A:
    cont_qnt_problemas+=1
    aux_resultado = 0
    aux = problema.split(';')
    aux_problema = aux[0]
    aux_classificacao = aux[1]
    if (problema_esta_na_arvore(arvore_1, aux_problema, 0, caminho))==1:
        aux_resultado = 1
        #print('a1')
        arq.writelines(aux_problema+';'+str(aux_classificacao)+';1;arvore_1\n')
    elif (problema_esta_na_arvore(arvore_2, aux_problema, 0, caminho))==1:
        aux_resultado = 1
        arq.writelines(aux_problema+';'+str(aux_classificacao)+';1;arvore_2\n')
        #print('a2')
    elif (problema_esta_na_arvore(arvore_3, aux_problema, 0, caminho))==1:
        aux_resultado = 1
        arq.writelines(aux_problema+';'+str(aux_classificacao)+';1;arvore_3\n')
        #print('a3')
    elif (problema_esta_na_arvore(arvore_4, aux_problema, 0, caminho))==1:
        aux_resultado = 1
        arq.writelines(aux_problema+';'+str(aux_classificacao)+';1;arvore_4\n')
        #print('a4')
    elif (problema_esta_na_arvore(arvore_5, aux_problema, 0, caminho))==1:
        aux_resultado = 1
        arq.writelines(aux_problema+';'+str(aux_classificacao)+';'+'1;arvore_5\n')
        #print('a5')
    else:
        aux_resultado = 0
        arq.writelines(aux_problema+';'+str(aux_classificacao)+';0;zica\n')
    
    if aux_resultado ==1 and aux_classificacao=='1':
        acuracia+=1
    elif aux_resultado==0 and aux_classificacao=='0':
        acuracia+=1

arq.close()
resultado = acuracia*100/cont_qnt_problemas

print ('Resultado '+ str(resultado))
print ('acurácia '+ str(acuracia))



