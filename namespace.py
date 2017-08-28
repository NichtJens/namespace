
def namespace(cls):
    """
    decorator that turns a class (either old- or new-style) into a namespace by
    applying staticmethod to all methods of cls not starting with an underscore
    """
    for name in cls.__dict__:
        if name.startswith("_"):
            continue
#        attr = getattr(cls, name)  # why does this not work?
        attr = cls.__dict__[name]
        static = staticmethod(attr)
        setattr(cls, name, static)

    return cls()


