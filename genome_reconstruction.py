import sys
import argparse
import string_reconstruction


def main():
    args_parser = argparse.ArgumentParser(description='This script dedicated \
                                          to the assembling genome topic.')
    args_parser.add_argument('-i', '--input',
                             type=str,
                             default='STDIN',
                             help='Input file name or \'STDIN\'. \
                             (Default STDIN) \
                             Terminate input from STDIN - Ctrl-Z or Ctrl-D')
    args = args_parser.parse_args()
    if args.input == 'STDIN':
        input_stream = sys.stdin
    else:
        try:
            input_stream = open(args.input, 'r')
        except(FileNotFoundError, IOError):
            print('File not found:', args.input)
            return
    input_strings = input_stream.readlines()
    list_of_kmers = string_reconstruction.clear_fasta_input(input_strings)
    kmers_alligning, reconstructed_string = \
        string_reconstruction.reconstruct_string(list_of_kmers)
    for i in range(len(kmers_alligning)):
        print(i*' ' + kmers_alligning[i])
    print(reconstructed_string)


if __name__ == '__main__':
    main()
