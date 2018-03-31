#!/bin/bash

for i in {1..100};
do
echo "Creating secret for mysql..."
kubectl create secret -n=prod-$i generic mysql-pass --from-file=password.txt

echo "Deploying mysql for wordpress..."
kubectl apply -f mysql-vol-$i.yaml
sleep 15
kubectl apply -f mysql-$i.yaml
sleep 15

echo "Deploying wordpress..."
kubectl apply -f wordpress-vol-$i.yaml
sleep 15
kubectl apply -f wordpress-$i.yaml
sleep 15
done
