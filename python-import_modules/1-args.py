import sys

if __name__ == "__main__":
    def print_arguments ():
     num_of_args = len(sys.argv) - 1 

if num_of_args == 0:
       print("0 argument.")
       print(":")
    elif num_of_args == 1
        print("1 argument:")
     else:
        print("{} arguments:".format(num_of_args))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
     
    print_arguments()