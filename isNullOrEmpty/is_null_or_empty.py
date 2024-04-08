def is_null_or_empty(param):
    if param is None:
        return True
    if isinstance(param, str):
        return param.strip() == ''
    elif isinstance(param, (list, dict)):
        return len(param) == 0
    else:
        return False
