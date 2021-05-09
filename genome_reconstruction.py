import sys
import argparse
import string_reconstruction


def main():
    args_parser = argparse.ArgumentParser(description='This script is \
                                          dedicated to the assembling \
                                          genome topic.')
    args_parser.add_argument('-i', '--input', required=True, type=str,
                             help='Input file name or \'STDIN\'. \
                             Terminate input from STDIN - Ctrl-Z or Ctrl-D')
    args_parser.add_argument('-o', '--output', type=str,
                             default='STDOUT',
                             help='Output file name or \'STDOUT\'. \
                             Default STDOUT.')
    args = args_parser.parse_args()
    if args.input == 'STDIN':
        input_stream = sys.stdin
    else:
        try:
            input_stream = open(args.input, 'r')
        except(FileNotFoundError, IOError):
            print('File not found:', args.input)
            return
    if args.output == 'STDOUT':
        output_stream = sys.stdout
    else:
        output_stream = open(args.output, 'w')
    input_strings = input_stream.readlines()
    list_of_kmers = string_reconstruction.clear_fasta_input(input_strings)
    try:
        kmers_alligning, reconstructed_string = \
            string_reconstruction.reconstruct_string(list_of_kmers)
        for i in range(len(kmers_alligning)):
            output_stream.write(i*' ' + kmers_alligning[i] + '\n')
        output_stream.write(reconstructed_string + '\n')
    except Exception:
        print('There is no way to reconstruct the DNA from these k-mers, \
try another data.')


if __name__ == '__main__':
    main()
