import sys

if __name__ == "__main__":
    def print_arguments ():
     arg_n = len(sys.argv) - 1 
     if arg_n == 0:
      print("0 argument.")
      print(":")
     elif arg_n == 1:
        print("1 argument:")
     else:
        print("{} arguments:".format(arg_n))

     for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
     
print_arguments()