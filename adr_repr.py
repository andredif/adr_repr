def repr_int(n: int):
    return str(n)


def repr_list(t: list):
    str_list = '['
    for l in t:
        if isinstance(l, int):
            str_list += ' '+repr_int(l)
        elif isinstance(l, list):
            str_list += repr_list(l)
        str_list += ',' if t.index(l)<(len(t)-1) else ''
    return str_list+']'

def repr_dict(t: dict):
    str_dict ='{'
    for i,k in enumerate(t.keys()):
        if isinstance(k, int):
            str_dict += ''+repr_int(k)+':'
        elif isinstance(k, list):
            str_dict += repr_list(k)+':'
        elif isinstance(k, dict):
            str_dict += repr_dict(k)+':'
        else :
            str_dict += repr_object+':'
        str_dict += x_repr(t.get(k))
        str_dict += ',' if i<(len(t)-1) else ''
    return str_dict + '}'

def repr_object(o: object):
    hex_id = hex(id(o))
    return '<'+ o.__class__.__name__ + ' object at ' + str(hex_id)+'>' 

class Example():
    a = 2


def x_repr(t: object):
    if isinstance(t, int):
        return repr_int(t)
    elif isinstance(t, list):
        return repr_list(t)
    
    