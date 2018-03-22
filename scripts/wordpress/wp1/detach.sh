#!/bin/bash

for i in {1..20};
do
echo "delete mysql and wordpress pods..."
kubectl delete -f wordpress-$i.yaml
kubectl delete -f mysql-$i.yaml
done
