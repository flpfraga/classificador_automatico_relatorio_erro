# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:53:10 2019

@author: Felipe Fraga
"""
def funcao_insere_arvore (arvore, lista_termo, lista_termo_2, cont_arvore, cont_termo, cont_termo_2):#funçao que insere elemento em um vetor representando uma árvore binária
    
    if cont_termo<len(lista_termo):
        termo_lista = lista_termo[cont_termo]
        termo_arvore = arvore[cont_arvore]
        
        if termo_arvore == '0':
            arvore[cont_arvore] = termo_lista
            cont_arvore = cont_arvore*2 + 1
            cont_termo +=1
            funcao_insere_arvore(arvore, lista_termo, lista_termo_2, cont_arvore, cont_termo, cont_termo_2)
            
        elif termo_arvore==termo_lista:
            cont_arvore = cont_arvore*2 + 1
            cont_termo +=1
            funcao_insere_arvore(arvore, lista_termo, lista_termo_2, cont_arvore, cont_termo, cont_termo_2)
        
        else:
            cont_arvore = cont_arvore*2 + 2
            funcao_insere_arvore(arvore, lista_termo, lista_termo_2, cont_arvore, cont_termo, cont_termo_2)
    
    elif cont_termo_2 < len(lista_termo_2):
        termo_lista_2 = lista_termo_2[cont_termo_2]
        termo_arvore = arvore[cont_arvore]
        
        if termo_arvore == '0':
            arvore[cont_arvore] = termo_lista_2
            cont_arvore = cont_arvore*2 + 2
            cont_termo_2 +=1
            funcao_insere_arvore(arvore, lista_termo, lista_termo_2, cont_arvore, cont_termo, cont_termo_2)
        
        elif termo_arvore==termo_lista_2:
            cont_arvore = cont_arvore*2 + 1
            cont_termo_2 +=1
            funcao_insere_arvore(arvore, lista_termo, lista_termo_2, cont_arvore, cont_termo, cont_termo_2)
        
        else:
            cont_arvore = cont_arvore*2 + 2
            funcao_insere_arvore(arvore, lista_termo, lista_termo_2, cont_arvore, cont_termo, cont_termo_2)
        
    else:
        
        if len(lista_termo_2) == 0:       
            termo_arvore = arvore[cont_arvore]
            
            if termo_arvore == '0':
                arvore[cont_arvore] = 'SIM'
                
        else:
            termo_arvore = arvore[cont_arvore]
            
            if termo_arvore == '0':
                arvore[cont_arvore] = 'SIM'
                
        return arvore
    
    return arvore

def funcao_salva_arvore_arquivo(arvore, nome):#função para salvar as arvores em arquivo
    pal_1 = ''
    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    arq = open('arquivos/'+nome, 'w')
    
    for pal in arvore:
        
        if 2**cont_1 <= cont_2:
            pal_1 +='\n'
            cont_1+=1
            cont_2 = 0
            
        if pal == '0':
            pal_1 +=str(cont_3)+';'
    
        else:
            pal_1 +=pal+';'
            
        cont_2+=1
        cont_3+=1
        
    arq.writelines(pal_1)
    
    arq.close()
    

arvore_0 = []
arvore_1 = []
arvore_2 = []
arvore_3 = []
arvore_4 = []
cont_3 = 0
tam = 5000

arvore_1 = []
cont_3 = 0

while cont_3 < 620:
    arvore_1.append('0')
    #print ('for')
    cont_3+=1
cont_3 = 0

arvore_2 = []
cont_3 = 0

while cont_3 < 1277:
    arvore_2.append('0')
    #print ('for')
    cont_3+=1
cont_3 = 0


arvore_3 = []
cont_3 = 0

while cont_3 < 745:
    arvore_3.append('0')
    #print ('for')
    cont_3+=1
cont_3 = 0

arvore_4 = []
cont_3 = 0

while cont_3 < 376:
    arvore_4.append('0')
    #print ('for')
    cont_3+=1
cont_3 = 0

arvore_5 = []
cont_3 = 0

while cont_3 < 209:
    arvore_5.append('0')
    #print ('for')
    cont_3+=1
cont_3 = 0

arq = open('arquivos/lista_final.csv', 'r')

for linha in arq:
    lista_termo = []
    lista_termo_2 = []
    primeira_parte = True
    palavra = linha.split(';')
    indice = palavra[0]
    
    if indice == '0':
        
        for pal in palavra:
            
            if primeira_parte:
                
                if pal == '-1':
                    primeira_parte = False
                    
                elif pal != '0' and pal != '' and pal !='\n':
                    lista_termo.append(pal.replace('\n', ''))
                    
            else:
                
                if pal != '0' and pal != '' and pal !='\n':
                    lista_termo_2.append(pal.replace('\n', ''))

        arvore_1 = funcao_insere_arvore(arvore_1, lista_termo, lista_termo_2,0, 0, 0)
        
    if indice == '1':
        
        for pal in palavra:
            
            if primeira_parte:
                
                if pal == '-1':
                    primeira_parte = False
                    
                elif pal != '1' and pal != '' and pal !='\n':
                    lista_termo.append(pal.replace('\n', ''))
                    
            else:
                
                if pal != '1' and pal != '' and pal !='\n':
                    lista_termo_2.append(pal.replace('\n', ''))
        
        arvore_2 = funcao_insere_arvore(arvore_2, lista_termo, lista_termo_2,0, 0, 0)
        
    elif indice == '2':
        
        for pal in palavra:
            
            if primeira_parte:
                
                if pal == '-1':
                    primeira_parte = False
                    
                elif pal != '2' and pal != '' and pal !='\n' and pal != ' ':
                    lista_termo.append(pal.replace('\n', ''))
                    
            else:
                
                if pal != '2' and pal != '' and pal !='\n' and pal != ' ':
                    lista_termo_2.append(pal.replace('\n', ''))

        arvore_3 = funcao_insere_arvore(arvore_3, lista_termo, lista_termo_2,0, 0, 0)
        
    elif indice == '3':
        
        for pal in palavra:
            
            if primeira_parte:
                
                if pal == '-1':
                    primeira_parte = False
                    
                elif pal != '3' and pal != '' and pal !='\n':
                    lista_termo.append(pal.replace('\n', ''))
                    
                    #funcao_print_lista(lista_termo)
            else:
                
                if pal != '3' and pal != '' and pal !='\n':
                    lista_termo_2.append(pal.replace('\n', ''))

        arvore_4 = funcao_insere_arvore(arvore_4, lista_termo, lista_termo_2,0, 0, 0)
        
    elif indice == '4':
        
        for pal in palavra:
            
            if primeira_parte:
                
                if pal == '-1':
                    primeira_parte = False
                    
                elif pal != '4' and pal != '' and pal !='\n':
                    lista_termo.append(pal.replace('\n', ''))
                    
            else:
                
                if pal != '4' and pal != '' and pal !='\n':
                    lista_termo_2.append(pal.replace('\n', ''))
       
        arvore_5 = funcao_insere_arvore(arvore_5, lista_termo, lista_termo_2,0, 0, 0)

arq.close()

funcao_salva_arvore_arquivo(arvore_1, 'arvore_1.csv')
funcao_salva_arvore_arquivo(arvore_2, 'arvore_2.csv')
funcao_salva_arvore_arquivo(arvore_3, 'arvore_3.csv')
funcao_salva_arvore_arquivo(arvore_4, 'arvore_4.csv')
funcao_salva_arvore_arquivo(arvore_5, 'arvore_5.csv')