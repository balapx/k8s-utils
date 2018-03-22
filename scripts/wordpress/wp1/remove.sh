for i in {1..20};
do
sed '14,66d' mysql-vol-$i.yaml > temp-$i.yaml
mv temp-$i.yaml mysql-vol-$i.yaml
done

for i in {1..20};
do
sed '16,71d' wordpress-vol-$i.yaml > temp-$i.yaml
mv temp-$i.yaml wordpress-vol-$i.yaml
done
