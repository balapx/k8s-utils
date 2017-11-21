#!/bin/bash -e

echo "Creating initial volume and write some data..."
kubectl apply -f scenario-7-vol.yaml 

echo "Creating snapshot of the volume..."
kubectl apply -f scenario-7-snap.yaml 

echo "writing more data for the initial volume"
kubectl apply -f scenario-7-data-vol.yaml

echo "Restoring pod from previous snapshot..."
kubectl apply -f pod-with-restored-vol.yaml

