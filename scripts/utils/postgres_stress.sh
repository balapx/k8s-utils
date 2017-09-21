#!/bin/sh

postgres=$(kubectl get pods -o wide | awk '/postgres/ { print $1 }')
for p in $postgres; do
  echo "Postgress Pods: $p"
  kubectl exec -i $p -- runuser -l postgres -c "/usr/lib/postgresql/9.5/bin/pgbench -i -s 6" &
  exit
done
