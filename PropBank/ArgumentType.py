from __future__ import annotations
from enum import Enum, auto

"""
Enumerated class for argument type.
"""

class ArgumentType(Enum):
    NONE = auto()
    PREDICATE = auto()
    ARG0 = auto()
    ARG1 = auto()
    ARG2 = auto()
    ARG3 = auto()
    ARG4 = auto()
    ARG5 = auto()
    ARGMNONE = auto()
    ARGMEXT = auto()
    ARGMLOC = auto()
    ARGMDIS = auto()
    ARGMADV = auto()
    ARGMCAU = auto()
    ARGMTMP = auto()
    ARGMPNC = auto()
    ARGMMNR = auto()
    ARGMDIR = auto()

    """
    The getArguments method takes an argumentsType string and returns the ArgumentType form of it.

    PARAMETERS
    ----------
    argumentsType : str 
        Type of the argument in string form
        
    RETURNS
    -------
    ArgumentType
        Type of the argument in ArgumentType form
    """
    @staticmethod
    def getArguments(argumentsType: str) -> ArgumentType:
        for type in ArgumentType:
            if argumentsType == type.name:
                return type
        return ArgumentType.NONE

    """
    The getPropbankType method takes an argumentType in ArgumentType form and returns the string form of it.

    PARAMETERS
    ----------
    argumentType : ArgumentType 
        Type of the argument in {@link ArgumentType} form
        
    RETURNS
    -------
    str
        Type of the argument in string form
    """
    @staticmethod
    def getPropbankType(argumentType: ArgumentType) -> str:
        if argumentType is None:
            return "NONE"
        return argumentType.name