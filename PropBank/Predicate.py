from PropBank.RoleSet import RoleSet


class Predicate(object):

    __lemma: str
    __roleSets: list

    """
    A constructor of Predicate class which takes lemma as input and initializes lemma with this input.
    The constructor also initializes the roleSets array.

    PARAMETERS
    ----------
    lemma : str
        Lemma of the predicate
    """
    def __init__(self, lemma: str):
        self.__lemma = lemma
        self.__roleSets = []

    """
    Accessor for lemma.

    RETURNS
    -------
    str
        lemma.
    """
    def getLemma(self) -> str:
        return self.__lemma

    """
    The addRoleSet method takes a RoleSet as input and adds it to the roleSets list.

    PARAMETERS
    ----------
    roleSet : RoleSet 
        RoleSet to be added
    """
    def addRoleSet(self, roleSet: RoleSet):
        self.__roleSets.append(roleSet)

    """
    The size method returns the size of the roleSets list.

    RETURNS
    -------
    int
        the size of the roleSets list.
    """
    def size(self) -> int:
        return len(self.__roleSets)

    """
    The getRoleSet method returns the roleSet at the given index.

    PARAMETERS
    ----------
    index : int 
        Index of the roleSet
        
    RETURNS
    -------
    RoleSet
        RoleSet at the given index.
    """
    def getRoleSet(self, index: int) -> RoleSet:
        return self.__roleSets[index]

    """
    Another getRoleSet method which returns the roleSet with the given roleSet id.

    PARAMETERS
    ----------
    roleId : str 
        Id of the searched roleSet

    RETURNS
    -------
    RoleSet
        RoleSet which has the given id.
    """
    def getRoleSetWithId(self, roleId: str) -> RoleSet:
        for roleSet in self.__roleSets:
            if roleSet.getId() == roleId:
                return roleSet
        return None
