#!/usr/bin/python3
def element_at(my_list, idx):
    last_index = len(my_list) - 1

    if idx < 0 or idx > last_index:
        return
    else:
        return my_list[idx]

