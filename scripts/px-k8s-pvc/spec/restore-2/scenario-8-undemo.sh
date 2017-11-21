#!/bin/bash -e

echo "Creating initial volume and write some data..."
kubectl delete -f scenario-8-vol.yaml 
sleep 2

echo "Creating snapshot of the volume..."
kubectl delete -f scenario-8-snap.yaml 
sleep 2

kubectl delete pods ankitkubefio -n dev

echo "writing more data for the initial volume"
kubectl delete -f scenario-8-data-vol.yaml
sleep 2

kubectl delete pods ankitkubefio -n dev

echo "Restoring pod from previous snapshot..."
kubectl delete -f scenario-8-restore-vol.yaml 

kubectl delete pods ankitkubefio -n dev
