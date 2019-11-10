from PropBank.ArgumentType import ArgumentType


class Role(object):

    _description: str
    _f: str
    _n: str

    """
    A constructor of Role class which takes description, f, and n as inputs and initializes corresponding with
    these inputs.

    PARAMETERS
    ----------
    description : str
        Description of the role
    f : str
        Argument Type of the role
    n : str
        Number of the role
    """
    def __init__(self, description: str, f: str, n: str):
        self._description = description
        self._f = f
        self._n = n

    """
    Accessor for description.

    RETURNS
    -------
    str
        description.
    """
    def getDescription(self) -> str:
        return self._description

    """
    Accessor for f.

    RETURNS
    -------
    str
        f.
    """
    def getF(self) -> str:
        return self._f

    """
    Accessor for n.

    RETURNS
    -------
    str
        n.
    """
    def getN(self) -> str:
        return self._n

    """
    Constructs and returns the argument type for this role.

    RETURNS
    -------
    ArgumentType
        Argument type for this role.
    """
    def getArgumentType(self) -> ArgumentType:
        return ArgumentType.getArguments("ARG" + self._f.upper())