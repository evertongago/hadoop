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
