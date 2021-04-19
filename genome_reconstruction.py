from string_reconstruction import reconstruct_string


list_of_kmers = []
tmp = input()
while tmp != '':
    list_of_kmers.append(tmp)
    tmp = input()
print(reconstruct_string(list_of_kmers))
