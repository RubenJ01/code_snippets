file_1 = open('monkerrage33size.txt', 'r').read().split(',')
file_2 = open('monkerrage100size.txt', 'r').read().split(',')
output = open('output.txt', 'w')

file1 = []
file2 = []

for x in file_1:
    file1.append(x.split("@"))

for x in file_2:
    file2.append(x.split("@"))

dict1 = {k: v for k, v in file1}
dict2 = {k: v for k, v in file2}

for x in dict1:
    if x not in dict2:
        # unique write to the output file
        output.write(f"{x}@{dict1[x]},")
    else:
        # not unique find the match and add the values up and then write to output file
        output.write(f"{x}@{int(dict1[x]) + int(dict2[x])},")

__author__ = "Ruben Eekhof"
