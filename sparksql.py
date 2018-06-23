import time

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import regexp_extract
from pyspark.sql.functions import sum

import re
import pprint

t0 = time.time()

sc = SparkContext("local", "My App")
sqlContext = SQLContext(sc)

logFiles = ["NASA_access_log_Jul95.gz","NASA_access_log_Aug95.gz"]

logData1 = sqlContext.read.text(logFiles[0])
logData = logData1.union(sqlContext.read.text(logFiles[1]))

# RDD
##logData = sqlContext.read.text(logFile)
##logData = sc.union(logDataList)

logData.show(5, truncate=False)

# modificados os campos date e request
logTable = logData.select(regexp_extract('value', r'^([^\s]+\s)', 1).alias('host'),
                        regexp_extract('value', r'^.*\[(\d\d/\w{3}/\d{4}):\d{2}:\d{2}:\d{2} -\d{4}]', 1).alias('date'),
                        regexp_extract('value', r'^.*\[\d\d/(\w{3})/\d{4}:\d{2}:\d{2}:\d{2} -\d{4}]', 1).alias('month'),
                        regexp_extract('value', r'^.*"(.+)"', 1).alias('request'),
                        regexp_extract('value', r'^.*"\s+([^\s]+)', 1).cast('integer').alias('status'),
                        #regexp_extract('value', r'^.*"\s+(400)', 1).cast('integer').alias('status'),
                        regexp_extract('value', r'^.*\s+(.+)$', 1).cast('integer').alias('content_size'))

logTable.show(5,truncate=False)

# hosts unicos
uniqHosts = logTable.groupby("host").count()
print "Hosts unicos: {}".format(uniqHosts.count())
uniqHosts.show(5,False)

'''
# checando requests mal formadas
err400 = logTable.filter(logTable['status']==400)
err400.show(5, truncate=False)

( logTable.filter(
  logTable["content_size"].isNull() ) 
  .groupby( "status").count() ).show()
'''

# total de request para cada status code
( logTable 
  .groupby( "status").count() ).show()

# montando a tabela de erros 404 por data  
dateTable = logTable \
  .filter(logTable['status']==404) \
  .groupby( ["date",logTable.month]).count().orderBy("month","date")

dateTable.show(dateTable.count())

  
# montando a tabela de erros 404 por request  
requestTable = logTable \
  .filter(logTable['status']==404) \
  .groupby("request").count()

requestTable.orderBy(requestTable['count'].desc()).show(5, False)

# somatoria dos bytes retornados
totalBytes = logTable.select( sum( logTable.content_size ).alias("total") )
print "Total em bytes: "
totalBytes.show()

# tempo
t1 = time.time()
print "---> executado em {} segundos".format(t1-t0)
###################


