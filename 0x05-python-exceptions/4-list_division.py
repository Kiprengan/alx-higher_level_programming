#!/user/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for m in range(0, list_length):
        try:
            divizion = my_list_1[m] / my_list_2[m]
        except TypeError:
            print("wrong type")
            divizion = 0
        except ZeroDivisionError:
            print("division by 0")
            divizion = 0
        except IndexError:
            print("out of range")
            divizion = 0
        finally:
            newList.append(divizion)
    return (newList)
