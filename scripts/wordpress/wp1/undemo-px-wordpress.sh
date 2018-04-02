#!/bin/bash -x

for i in {1..100};
do
echo "Deleting secret for mysql..."
kubectl delete secret -n=prod-$i mysql-pass

echo "Deleting wordpress..."
kubectl delete -f wordpress-$i.yaml

echo "Deleting mysql for wordpress..."
kubectl delete -f mysql-$i.yaml
sleep 20
done
