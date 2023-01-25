#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(0, list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                new_list.append(result)
            except TypeError as e:
                print("wrong type")
                new_list.append(0)
            except ZeroDivisionError as e:
                new_list.append(0)
                print("division by 0")
            except IndexError as e:
                new_list.append(0)
                print("out of range")
    except Exception as e:
        print(e)
    finally:
        return new_list
