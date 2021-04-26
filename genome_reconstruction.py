from string_reconstruction import fasta_input, reconstruct_string


list_of_kmers = fasta_input()
print(reconstruct_string(list_of_kmers))
