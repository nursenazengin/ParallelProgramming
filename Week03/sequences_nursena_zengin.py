def remove_duplicates(seq: list) -> list:
    return list(set(seq))



def list_counts(seq: list) -> dict:
    new_dict = {}
    for i in range(len(seq)):
        n = seq[i]              
        new_dict[n] = seq.count(n) 
    return new_dict



def reverse_dict(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():  
        new_dict[value] = key
    return new_dict
