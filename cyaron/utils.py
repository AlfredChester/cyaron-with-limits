def ati(array):
    """ati(array) -> list
    Convert all the elements in the array and return them in a list.
    """
    return [int(i) for i in array]


def list_like(data):
    """list_like(data) -> bool
    Judge whether the object data is like a list or a tuple.
    object data -> the data to judge
    """
    return isinstance(data, tuple) or isinstance(data, list)


def int_like(data):
    is_int = False
    try:
        is_int = is_int or isinstance(data, long)
    except NameError:
        pass
    is_int = is_int or isinstance(data, int)
    return is_int


def str_to_lines(str):
    lines = str.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

    while len(lines) > 0 and len(lines[len(lines) - 1]) == 0:
        del lines[len(lines) - 1]
    return lines


def make_unicode(data):
    return str(data)


def unpack_kwargs(funcname, kwargs, arg_pattern):
    rv = {}
    kwargs = kwargs.copy()
    for tp in arg_pattern:
        if list_like(tp):
            k, v = tp
            rv[k] = kwargs.get(k, v)
            try:
                del kwargs[k]
            except KeyError:
                pass
        else:
            error = False
            try:
                rv[tp] = kwargs[tp]
                del kwargs[tp]
            except KeyError as e:
                error = True
            if error:
                raise TypeError(
                    "{}() missing 1 required keyword-only argument: '{}'".format(
                        funcname, tp
                    )
                )
    if kwargs:
        raise TypeError(
            "{}() got an unexpected keyword argument '{}'".format(
                funcname, next(iter(kwargs.items()))[0]
            )
        )
    return rv
