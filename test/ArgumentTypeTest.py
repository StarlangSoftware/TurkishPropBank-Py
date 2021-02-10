import unittest

from PropBank.ArgumentType import ArgumentType


class ArgumentTypeTest(unittest.TestCase):

    def test_ArgumentType(self):
        self.assertEqual(ArgumentType.getArguments("arg0"), ArgumentType.ARG0)
        self.assertEqual(ArgumentType.getArguments("argmdis"), ArgumentType.ARGMDIS)
        self.assertEqual(ArgumentType.getArguments("Arg1"), ArgumentType.ARG1)
        self.assertEqual(ArgumentType.getArguments("Argmdir"), ArgumentType.ARGMDIR)
