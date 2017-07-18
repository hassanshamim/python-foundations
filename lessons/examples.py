def mystery_function(data):
    arg_type = type(data)
    data += arg_type(range(5))
    return data
