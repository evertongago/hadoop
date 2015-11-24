<h2> Tutorial </h2>
<p align="justify">
Este projeto apresenta um recomendador de conteúdo, criado a partir do Apache Hadoop e Apache Mahout. Criamos esta arquitetura a partir de uma plataforma Linux (Ubuntu 12.0.4) 64 bits e Docker 1.5.0. Os  procedimentos a seguir descrevem passo a passo a configuração do ambiente e a execução do recomendador de conteúdo.
</p>
<p align="justify">
Após descarregar o projeto, entre no diretório e execute o seguinte comando para executar a build do Docker:
</p>

> docker build -t instance-name .

<p align="justify" style="padding-top: 15px;">
Certifique-se de que a build foi executada corretamente e de que todos os downloads foram executados. Agora você pode criar uma instância Docker dessa máquina. Veja:
</p>

> docker run -d -P --name instance-name instance-name

<p align="justify" style="padding-top: 15px;">
Execute o comando a seguir para descobrir a porta ssh que a instância foi disponibilizada:
</p>

> docker port instance-name

<p align="justify" style="padding-top: 15px;">
Agora você pode se conectar a instância usando ssh. A senha é: 'screencast'.
</p>

> ssh root@localhost -p ssh-port

<p align="justify" style="padding-top: 15px;">
Uma vez conectado a instãncia, crie uma formate a partição do Hadoop para que possamos trabalhar com arquivos. Veja:
</p>

> hadoop namenode -format

<p align="justify" style="padding-top: 15px;">
Inicie o Hadoop.
</p>

> start-all.sh

<p align="justify" style="padding-top: 15px;">
Mova o arquivo <b>show_recommendations.py?dl=0</b> para o diretório <b>ml-100k</b> e renomeie.
</p>

> mv show_recommendations.py?dl=0 ml-100k/show_recommendations.py

<p align="justify" style="padding-top: 15px;">
Entre no diretório <b>ml-100k</b>.
</p>

> cd ml-100k

<p align="justify" style="padding-top: 15px;">
Registre o arquivo <b>u.data</b> no Hadoop File System.
</p>

> hadoop fs -put u.data u.data

<p align="justify" style="padding-top: 15px;">
Execute o Job de recomendação de conteúdo do Mahout e aguarde o processamento.
</p>

> hadoop jar /opt/mahout-distribution-0.9/mahout-distribution-0.10.0-job.jar org.apache.mahout.cf.taste.hadoop.item.RecommenderJob -s SIMILARITY_COOCCURRENCE --input u.data --output output

<p align="justify" style="padding-top: 15px;">
Recupere a lista de recumendação do Hadoop File System e salve em um arquivo chamado output.txt
</p>

> hadoop fs -getmerge output output.txt

<p align="justify" style="padding-top: 15px;">
O arquivo output.txt contém o identificador do usuário, seguido de uma lista de conteúdos (id e nota) a serem recomendados. Escrevemos uma rotina Python que apresenta os resultados de forma mais legível. Veja a seguir como executar essa rotina:
</p>

> python show_recommendations.py user-id u.data u.item output.txt

<p align="justify" style="padding-top: 15px;">
Substitua o atributo user-id pelo identificador do usuário que deseja fazer a recomendação, por exemplo: 10.
</p>
