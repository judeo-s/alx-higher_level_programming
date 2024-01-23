def list_division(my_list_1, my_list_2, list_length):
    '''
    A function that divides element by element 2 lists.

    Args:
        my_list_1: list
        my_list_2: list
        list_length: int
    Returns:
        quotients: list
    '''
    quotients = []

    for i in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            quotients.append(quotient)

    return quotients
