<h2>Introdução</h2>
<p>
Este projeto apresenta um recomendador de conteúdo, criado a partir do Apache Hadoop e Apache Mahout. Criamos esta arquitetura a partir de uma plataforma Linux (Ubuntu 12.0.4) 64 bits e Docker 1.5.0. Os  procedimentos a seguir descrevem passo a passo a configuração do ambiente e a execução do recomendador de conteúdo.
</p>
<ul>
  <li>Comando 1</li>
  <li>Comando 2</li>
</ul>
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
