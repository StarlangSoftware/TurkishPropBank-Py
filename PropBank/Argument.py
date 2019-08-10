class Argument(object):

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
            self.argumentType = argument[0:argument.index("$")]
            self.id = argument[argument.index("$") + 1:]
        else:
            self.argumentType = "NONE"

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
        self.argumentType = argumentType
        self.id = id

    """
    Accessor for argumentType.
    
    RETURNS
    -------
    str
        argumentType.
    """
    def getArgumentType(self) -> str:
        return self.argumentType

    """
    Accessor for id.

    RETURNS
    -------
    str
        id.
    """
    def getId(self) -> str:
        return self.id

    """
    __str__ converts an Argument to a string. If the argumentType is "NONE" returns only "NONE", otherwise
    it returns argument string which is in the form of argumentType$id

    RETURNS
    -------
    str
        string form of argument
    """
    def __str__(self) -> str:
        if self.argumentType == "NONE":
            return self.argumentType
        else:
            return self.argumentType + "$" + self.id