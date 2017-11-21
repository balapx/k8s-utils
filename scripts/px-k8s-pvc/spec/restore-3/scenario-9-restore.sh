#!/bin/bash -e

echo "Creating initial volume and write some data..."
kubectl apply -f scenario-9-vol.yaml 
sleep 120

echo "Creating snapshot of the volume..."
kubectl apply -f scenario-9-snap.yaml 
sleep 5

kubectl delete pods ankitkubefio -n default

echo "writing more data for the initial volume"
kubectl apply -f scenario-9-data-vol.yaml
sleep 120

kubectl delete pods ankitkubefio -n default

echo "Restoring pod from previous snapshot..."
kubectl apply -f scenario-9-restore-vol.yaml 

kubectl delete pods ankitkubefio -n default
