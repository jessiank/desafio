#  desafio junho 2018
# prototipo em Python para familiarizacao com os dados

import gzip
import pprint
import re

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
              if host not in dicHosts.keys():
                 dicHosts[host]=1
              else:
                 dicHosts[host]+=1
                 
              # contagem dos erros 404
              if fields.group(7)=='404':
                  err404+=1
                  # separando as datas somente no caso de erro 404
                  tstamp = fields.group(4)
                  #print tstamp
                  dia = re.search('^\[(.*):..:..:..',tstamp)
                  if dia:
                    ddmmaa = dia.group(1)
                    if ddmmaa not in dicDias404.keys():
                       dicDias404[ddmmaa]=1
                    else:
                       dicDias404[ddmmaa]+=1
                 
              # processamento do campo com a URL
              httpreq = fields.group(6)
              httpparams = httpreq.split()
              numpf = len(httpparams)
              if numpf not in dicURLfield.keys():
                 dicURLfield[numpf] = 1
              else:
                 dicURLfield[numpf] += 1
                 
              # visualizando requisicao HTTP com mais de 4 parametros por curiosidade   
              if numpf > 4:
                 print httpreq
                 # curiosidade
                 #print host
                 #print line
                 
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
print i

#1. total de hosts unicos
print "HOSTS UNICOS"
print len(dicHosts.keys())

#2. total de erros 404
print err404

# total de bytes
print "TOTAL DE BYTES"
print totalBytes

# dicionario URL -> total de erros 404 por URL
#pprint.pprint(dicURL)

# contagem de parametros no campo de URL
pprint.pprint(dicURLfield)

# erros 404 por data
pprint.pprint(dicDias404)

# imprimindo dicionario ordenado pelos valores
'''
j=1
for w in sorted(dicURL, key=dicURL.get, reverse=True):
 if j<=5: # somente as 5 primeiras linhas
	print w, dicURL[w]
	j+=1
        
'''    

