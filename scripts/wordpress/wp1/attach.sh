#!/bin/bash

for i in {1..20};
do
echo "Deploy mysql and wordpress pods..."
kubectl apply -f mysql-$i.yaml
sleep 5
kubectl apply -f wordpress-$i.yaml
sleep 10
done
