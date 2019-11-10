class Argument(object):

    __argumentType: str
    __id: str

    """
    A constructor of Argument class which takes argument string which is in the form of argumentType$id
    and parses this string into argumentType and id. If the argument string does not contain '$' then the
    constructor return a NONE type argument.

    PARAMETERS
    ----------
    argument : str
        Argument string containing the argumentType and id
    """
    def __init__(self, argument: str):
        if "$" in argument:
            self.__argumentType = argument[0:argument.index("$")]
            self.__id = argument[argument.index("$") + 1:]
        else:
            self.__argumentType = "NONE"

    """
    Another constructor of Argument class which takes argumentType and id as inputs and initializes corresponding attributes

    PARAMETERS
    ----------
    argumentType : str 
        Type of the argument
    id : str 
        Id of the argument
    """
    def initWithId(self, argumentType: str, id: str):
        self.__argumentType = argumentType
        self.__id = id

    """
    Accessor for argumentType.
    
    RETURNS
    -------
    str
        argumentType.
    """
    def getArgumentType(self) -> str:
        return self.__argumentType

    """
    Accessor for id.

    RETURNS
    -------
    str
        id.
    """
    def getId(self) -> str:
        return self.__id

    """
    __str__ converts an Argument to a string. If the argumentType is "NONE" returns only "NONE", otherwise
    it returns argument string which is in the form of argumentType$id

    RETURNS
    -------
    str
        string form of argument
    """
    def __str__(self) -> str:
        if self.__argumentType == "NONE":
            return self.__argumentType
        else:
            return self.__argumentType + "$" + self.__id