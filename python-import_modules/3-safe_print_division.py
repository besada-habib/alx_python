def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result

if __name__ == "__main__":
    safe_print_division()
