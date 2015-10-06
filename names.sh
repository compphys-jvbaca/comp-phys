i='0';
while [ $i -lt 100 ];
do 
sleep $(python -S -c "import random;
print random.randint(100, 500)")
say $(python -S -c "import random ;
print random.choice(['Terry', 'Zowshung', 'Ian', 'James', 'Howard', 'Monica', 'Matt', 'Matt', 'Zach', 'Jacob', 'Ritesh'])");
done