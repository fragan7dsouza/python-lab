def tup_to_dict(tup_list):
    result_dict={}
    for item in tup_list:
        if len(item)==2:
            key,value=item
            result_dict[key]=value
        else:
            print("skipping tuple because not exactly 2 elements")
    return result_dict
tup_list=[("a",1),("b",2),("c",3),("d",4)]
result_dict=tup_to_dict(tup_list)
print(result_dict)
