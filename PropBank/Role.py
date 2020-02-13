from PropBank.ArgumentType import ArgumentType


class Role(object):

    __description: str
    __f: str
    __n: str

    def __init__(self, description: str, f: str, n: str):
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
        self.__description = description
        self.__f = f
        self.__n = n

    def getDescription(self) -> str:
        """
        Accessor for description.

        RETURNS
        -------
        str
            description.
        """
        return self.__description

    def getF(self) -> str:
        """
        Accessor for f.

        RETURNS
        -------
        str
            f.
        """
        return self.__f

    def getN(self) -> str:
        """
        Accessor for n.

        RETURNS
        -------
        str
            n.
        """
        return self.__n

    def getArgumentType(self) -> ArgumentType:
        """
        Constructs and returns the argument type for this role.

        RETURNS
        -------
        ArgumentType
            Argument type for this role.
        """
        return ArgumentType.getArguments("ARG" + self.__f.upper())
