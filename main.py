# import important libraries
import argparse
import math

# encryption function
def encrypt(input_file, output_file):

    print("Encrypting file:", input_file, "to", output_file)

    # open and read the file we want to encrypt
    with open(input_file, "r", encoding="utf-8") as file:
        file_content = file.read()

    result = ""

    # in this loop:
    # every letter have a number in ASCII
    # we power this number to 2 and return back as char
    
    for i in file_content:
    	shifted = ord(i) ** 2
    	result += chr(shifted)
    
    # then we store the output into the output file
    with open(output_file, "a", encoding="utf-8") as file:
        file.write(result)

    print("file: ", input_file, " Encrypted to: ", output_file)

# decryption function
def decrypt(input_file, output_file):
    
    print("Decrypting file:", input_file, "to", output_file)

    # open and read the encrypted file
    with open(input_file, "r", encoding="utf-8") as file:
        file_content = file.read()

    result = ""

    # in this loop we take the squar of the letter in the encrypted file
    # so we get the original value which we have powered it to 2
    # and retuen the number to letter again
    for i in file_content:
    	shifted = int(math.sqrt(ord(i)))
    	result += chr(shifted)

    # store the decrypted data into the output file
    with open(output_file, "a", encoding="utf-8") as file:
        file.write(result)

    print("file: ", input_file, " Decrypted to: ", output_file)

# main function
def main():
    # declear the flags and argements
    parser = argparse.ArgumentParser(
        prog='\033[1;34mDR. Crypto\n\033[0m',
        description='encrypt or decrypt any file you want')
    parser.add_argument("-i", "--input", help="the file to encrypt/decrypt")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the file")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file")
    parser.add_argument("-o", "--output", help="where is the output file")
    args = parser.parse_args()

    # check what user add and send them to functions to do his work
    if args.encrypt:
        if args.output:
            encrypt(args.input, args.output)
        else:
            print("Please specify the input and output file using -i and -o option. \nex: -i input.txt -o output.txt")
    elif args.decrypt:
        if args.output:
            decrypt(args.input, args.output)
        else:
            print("Please specify the input and output file using -i and -o option. \nex: -i input.txt -o output.txt")
    else:
        print("Please specify either -e or -d option.\ntry flag -h to learn more")
   
# run the script     
main()
    
    
