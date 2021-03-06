#!/bin/bash -x

echo "Deleting secret for mysql..."
kubectl delete secret mysql-pass

echo "Deleting wordpress..."
kubectl delete -f wordpress.yaml
kubectl delete -f wordpress-sc.yaml

echo "Deleting mysql for wordpress..."
kubectl delete -f mysql.yaml
kubectl delete -f mysql-sc.yaml
