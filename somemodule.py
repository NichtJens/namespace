
"""
example module to demonstrate the use of the namespace decorator
to hide internal functions and only directly expose one to a user
"""

from namespace import namespace


@namespace
class internal:
    """
    namespace to hide internal functions
    which would usually be prepended with an underscore
    """

    def double(x):
        return 2 * x

    def triple(x):
        return 3 * x



def important(x):
    """the function that a user should be able to see"""
    return internal.double(x) + internal.triple(x)


