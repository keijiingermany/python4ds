def ft_filter(function, iterable):
""" simple reproduction of built_in filter functiion"""

    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
