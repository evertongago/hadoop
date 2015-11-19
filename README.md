## H2 Introdução
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
<div style="background-color: gainsboro;">
docker run -d -P --name instance-name instance-name
</div>
<p align="justify" style="padding-top: 15px;">
Execute o comando a seguir para descobrir a porta ssh que a instância foi disponibilizada:
</p>
<div style="background-color: gainsboro;">
docker port instance-name
</div>
<p align="justify" style="padding-top: 15px;">
Agora você pode se conectar a instância usando ssh. Veja:
</p>
<div style="background-color: gainsboro;">
ssh root@localhost -p ssh-port
</div>

sudo docker build -t <instance_name> .
sudo docker run -d -P --name <instance_name> <instance_name>
sudo docker port <instance_name>
ssh root@localhost -p <ssh_port>
stop-all.sh
hadoop namenode -format
start-all.sh
cd /root/ml-100k
hadoop fs -put u.data u.data
hadoop jar /opt/mahout-distribution-0.9/mahout-core-0.9-job.jar org.apache.mahout.cf.taste.hadoop.item.RecommenderJob -s SIMILARITY_COOCCURRENCE --input u.data --output output
hadoop fs -getmerge output output.txt
python show_recommendations.py <user_id> u.data u.item output.txt
