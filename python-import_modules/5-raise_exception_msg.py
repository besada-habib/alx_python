def raise_exception_msg(message=""):
 raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg

try: 
    raise NameError("")
except NameError:
    print (raise_exception_msg)
    raise