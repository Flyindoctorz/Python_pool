def ft_filter(fonction, iterable):
    """ Return the elements from iterable"""
    """ when fonction(element) is true"""
    return [element for element in iterable if fonction(element)]
