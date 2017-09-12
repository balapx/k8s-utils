while true;
do
kubectl get pods -o wide | awk '/mysql/ { print $1 }' | xargs -I{} kubectl exec -i {} -- runuser -c "mysqlslap -u sysadmin -pmypassword --concurrency=5 --iterations=20 --number-int-cols=2 --number-char-cols=3 --auto-generate-sql";
done
