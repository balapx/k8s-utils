for i in {1..20};
do
cp -r /home/centos/bala/wordpress/wp1/wordpress-$i.yaml /home/centos/bala/wordpress/wp1/wordpress-vol-$i.yaml
cp -r /home/centos/bala/wordpress/wp1/mysql-$i.yaml /home/centos/bala/wordpress/wp1/mysql-vol-$i.yaml
done
