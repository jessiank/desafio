Inicialmente fiz um prototipo em Python sem utilizar Spark para 
ter mais certeza do caminho a ser trilhado, utilizando as estruturas
de dados comuns tais como dicionarios e loops

O arquivo desse prototipo tambem foi disponibilizado no GitHub,
com o nome "prototipo.py"

A rotina em Spark + Python utilizou a biblioteca pyspark.sql
e foi disponibilizada com o nome "sparksql.py"

Aproveitei tambem para comparar os tempos de processamento dos
dois codigos, sendo bem claro que o uso de Spark ganhou "de lavada"
do codigo em Python puro (117 segundos contra 450 segundos)
 
As respostas foram disponibilizadas no arquivo "respostas.txt"

Para responder ao desafio, foram utilizadas as seguintes paginas na web

1. stackoverflow.com

- diversas questoes e respostas dos usuarios do site

2. melhor texto comparando group by key com reduce by key:

https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html

3. como ler os dados sem utilizar Hadoop

https://blueplastic.gitbooks.io/how-to-light-your-spark-on-a-stick/content/launch_the_scala_shell/reading_&_writing_to_text_files.html

4. escolhendo a melhor maneira de utilizar Spark em Python adaptada a minha experiencia

https://www.codementor.io/jadianes/spark-python-rdd-basics-du107x2ra

http://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=regex

https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PySpark_SQL_Cheat_Sheet_Python.pdf

5. decifrando DataFrames para ordenar melhor o agrupamento de erros 404 por data

https://databricks.com/blog/2016/02/09/reshaping-data-with-pivot-in-apache-spark.html

https://stackoverflow.com/questions/46809879/convert-pyspark-groupeddata-object-to-spark-dataframe

- objeto Column trata-se apenas de um simbolo, deve ser usado com select

https://stackoverflow.com/questions/31124131/viewing-the-content-of-a-spark-dataframe-column

