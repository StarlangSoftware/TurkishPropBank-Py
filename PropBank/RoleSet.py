from PropBank.Role import Role


class RoleSet(object):

    __id: str
    __name: str
    __roles: list

    """
    A constructor of RoleSet class which takes id and name as inputs and initializes corresponding attributes
    with these inputs.

    PARAMETERS
    ----------
    id : str
        Id of the roleSet
    name : str
        Name of the roleSet
    """
    def __init__(self, _id: str, name: str):
        self.__id = _id
        self.__name = name
        self.__roles = []

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
    Accessor for name.

    RETURNS
    -------
    str
        name.
    """
    def getName(self) -> str:
        return self.__name

    """
    The size method returns the size of the roles list.

    RETURNS
    -------
    int
        the size of the roles list.
    """
    def size(self) -> int:
        return len(self.__roles)

    """
    The addRole method takes a Role as input and adds it to the roles list.

    PARAMETERS
    ----------
    role : Role 
        Role to be added
    """
    def addRole(self, role: Role):
        self.__roles.append(role)

    """
    The getRole method returns the role at the given index.

    PARAMETERS
    ----------
    index : int 
        Index of the role
        
    RETURNS
    -------
    Role
        Role at the given index.
    """
    def getRole(self, index: int) -> Role:
        return self.__roles[index]

    """
    Finds and returns the role with the given argument number n. For example, if n == 0, the method returns
    the argument ARG0.
    
    PARAMETERS
    ----------
    n : str
        Argument number
        
    RETURNS
    -------
    Role
        The role with the given argument number n.
    """
    def getRoleWithArgument(self, n: str) -> Role:
        for role in self.__roles:
            if role.getN() == n:
                return role
