while true;
do
postgres=$(kubectl get pods -o wide | grep "postgres" | grep "Running" | shuf | awk '{print $1}' | head -n 1)
kubectl delete pods $postgres
kubectl get pods -o wide
sleep 5
done
