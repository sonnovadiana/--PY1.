def delete(your_list, index=None):
    del your_list[-1]
    if index != None:
        del your_list[index]

    return your_list
