
root@master:~/sql# kubectl get pods -o wide
NAME                     READY     STATUS    RESTARTS   AGE       IP          NODE
mysql-1520757855-6d6vp   1/1       Running   0          12m       10.40.0.1   minion-4

root@minion-4:/home/ubuntu# docker ps | grep mysql
d1c6e1aae9fd        cdfa8cc50c33                               "docker-entrypoint.sh"   3 minutes ago       Up 3 minutes                            k8s_mysql_mysql-1520757855-6d6vp_default_6bc626ce-89de-11e7-9aae-022185d04910_0
79e8836132c1        gcr.io/google_containers/pause-amd64:3.0   "/pause"                 13 minutes ago      Up 13 minutes                           k8s_POD_mysql-1520757855-6d6vp_default_6bc626ce-89de-11e7-9aae-022185d04910_0
root@minion-4:/home/ubuntu# docker exec -it d1c6e1aae9fd bash
root@mysql-1520757855-6d6vp:/# mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.6.37 MySQL Community Server (GPL)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

mysql> create user "systemadmin" identified by "password";
Query OK, 0 rows affected (0.01 sec)

mysql> grant all on *.* to sysadmin;
Query OK, 0 rows affected (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO sysadmin@localhost IDENTIFIED  BY 'mypassword';
Query OK, 0 rows affected (0.00 sec)

