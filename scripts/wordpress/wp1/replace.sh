for i in {3..20};
do
sed -i 's/prod-1/prod-$i/g' wordpress-$i.yaml
done
