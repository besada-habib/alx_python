

def safe_print_division(a, b):
     try:
       result = a / b
     except ZeroDivisionError:
       result = None
     finally:
      if __name__ == "__main__":
         print("Inside result: {}".format(result))
     return result
