from __future__ import annotations
from enum import Enum, auto


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

    @staticmethod
    def getArguments(argumentsType: str) -> ArgumentType:
        for type in ArgumentType:
            if argumentsType == type.name:
                return type
        return ArgumentType.NONE

    @staticmethod
    def getPropbankType(argumentType: ArgumentType) -> str:
        if argumentType is None:
            return "NONE"
        return argumentType.name