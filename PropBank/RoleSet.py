from PropBank.Role import Role


class RoleSet(object):

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
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.roles = []

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
    Accessor for name.

    RETURNS
    -------
    str
        name.
    """
    def getName(self) -> str:
        return self.name

    """
    The size method returns the size of the roles list.

    RETURNS
    -------
    int
        the size of the roles list.
    """
    def size(self) -> int:
        return len(self.roles)

    """
    The addRole method takes a Role as input and adds it to the roles list.

    PARAMETERS
    ----------
    role : Role 
        Role to be added
    """
    def addRole(self, role: Role):
        self.roles.append(role)

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
        return self.roles[index]