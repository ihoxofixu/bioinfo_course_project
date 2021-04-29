from string_reconstruction import fasta_input, reconstruct_string


fin = open('input.txt', 'r')
list_of_kmers = fasta_input(fin.readlines())
print(reconstruct_string(list_of_kmers))
fin.close()
