while true;
do
kubectl get pods -o wide -n=kube-system
postgres=$(kubectl get pods -o wide -n=kube-system | grep "portworx" | grep "Running" | shuf | awk '{print $1}' | head -n 1)
kubectl delete pods $postgres -n=kube-system
kubectl get pods -o wide -n=kube-system
sleep 120
done
