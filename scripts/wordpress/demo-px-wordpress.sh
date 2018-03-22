#!/bin/bash

echo "Creating secret for mysql..."
tr --delete '\n' <password.txt >.strippedpassword.txt && mv .strippedpassword.txt password.txt
kubectl create secret -n=prod-1 generic mysql-pass --from-file=password.txt

echo "Deploying mysql for wordpress..."
kubectl apply -f mysql-sc.yaml
kubectl apply -f mysql.yaml

echo "Deploying wordpress..."
kubectl apply -f wordpress-sc.yaml
kubectl apply -f wordpress.yaml
