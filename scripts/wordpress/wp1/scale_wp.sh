#!/bin/bash

for i in {1..20};
do
echo "Scaling wordpress pods..."
kubectl scale deployment wordpress -n=prod-$i --replicas=10
done
