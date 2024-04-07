def is_null_or_empty(param):
    if param is None:
        return True
    if hasattr(param, '__len__') and len(param) == 0:
        return True
    return False