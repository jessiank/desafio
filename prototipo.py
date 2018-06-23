#  desafio junho 2018
# prototipo em Python para familiarizacao com os dados
from time import time
import gzip
import pprint
import re

t0 = time()

i=0
err404=0
totalBytes=0

# dicionario de Hosts
dicHosts = {}
# dicionario para cada URL problematica
dicURL = {}
# dicionario de erros 404 em cada dia
dicDias404 = {}
# dicionario para processar o campo da URL
dicURLfield = {}

# lista de arquivos
arq = ['NASA_access_log_Jul95.gz','NASA_access_log_Aug95.gz']

for file in arq:
    l=0
    print(file)
    
    with gzip.open(file,"rb") as Log:
        
        for line in Log:
            
            i+=1
            l+=1
            #words = line.split()
            fields = re.search('(.+) (.+) (.+) (.+) (.+) "(.+)" (.+) (.+)',line)
            if fields:
            
              # contagem dos hosts unicos
              host = fields.group(1)
              dicHosts[host]=1
              
              # processamento do campo com a URL
              httpreq = fields.group(6)
              httpparams = httpreq.split()
              
              '''
              numpf = len(httpparams)
              if numpf not in dicURLfield.keys():
                 dicURLfield[numpf] = 1
              else:
                 dicURLfield[numpf] += 1
                 
              # visualizando requisicao HTTP com mais de 4 parametros por curiosidade   
              if numpf > 4:
                 print httpreq
                 # outra curiosidade
                 #print host
                 #print line
              '''
              
              # contagem dos erros 404
              if fields.group(7)=='404':
                  err404+=1
                  
                  # montando dicionario de quantidade de erro 404 para cada URL
                  url = httpparams[1]
                  
                  if url not in dicURL.keys():
                     dicURL[url] = 1
                  else:
                     dicURL[url] += 1
                  
                  # separando as datas somente no caso de erro 404
                  tstamp = fields.group(4)
                  #print tstamp
                  dia = re.search('^\[(.*):..:..:..',tstamp)
                  if dia:
                      
                    ddmmaa = dia.group(1)
                    splitdate = re.search('(.+)\/(.+)\/(.+)',ddmmaa)
                    
                    if splitdate:
                        mes = splitdate.group(2)
                        pass
                    
                    # particionando o dicionario 
                    if mes not in dicDias404.keys():
                        dicDias404[mes]={}
                        
                    if ddmmaa not in dicDias404[mes].keys():
                       dicDias404[mes][ddmmaa]=1
                    else:
                       dicDias404[mes][ddmmaa]+=1
                 
              #print i  
                
              # somatoria dos bytes trafegados
              try:
                siz = int(fields.group(8))
                totalBytes += siz
              except ValueError:
                # zero bytes
                pass            
                
            else: # caso a expressao regular seja incompativel, encontramos alguma linha estranha
            
              print "==========================="
              print line

# total de linhas    
print "LINHAS: {}".format(i)

#1. total de hosts unicos
print "HOSTS UNICOS: {}".format( len(dicHosts.keys()) )

#2. total de erros 404
print "TOTAL ERROS 404: {}".format(err404)

# total de bytes
print "TOTAL DE BYTES: {}".format(totalBytes)
 

# dicionario URL -> total de erros 404 por URL
#pprint.pprint(dicURL)

# contagem de parametros no campo de URL
##pprint.pprint(dicURLfield)

# erros 404 por data
print "ERROS 404 POR DATA:"
pprint.pprint(dicDias404)

# imprimindo URL com erro 404 ordenadas pelos valores
print "TOP 5 URLS INEXISTENTES:"
j=1
for w in sorted(dicURL, key=dicURL.get, reverse=True):
 if j<=5: # somente as 5 primeiras linhas
	print w, dicURL[w]
	j+=1
        

t1 = time()
print "---> executado em {} segundos".format(t1-t0)
