def remove_duplicates(lst):
    ret_lst = []
    for i in lst:
        if i not in ret_lst:
            ret_lst.append(i);
    return ret_lst
    