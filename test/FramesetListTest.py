import unittest

from PropBank.FramesetList import FramesetList


class FramesetListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.framesetList = FramesetList()

    def test_Frames(self):
        self.assertEqual(17692, self.framesetList.size())

    def test_ArgSize(self):
        count = 0
        for i in range(self.framesetList.size()):
            count += len(self.framesetList.getFrameSet(i).getFramesetArguments())
        self.assertEqual(29761, count)

    def test_Case(self):
        caseList = {}
        for i in range(self.framesetList.size()):
            for argument in self.framesetList.getFrameSet(i).getFramesetArguments():
                if argument.getGrammaticalCase() != "":
                    if "abl" in argument.getGrammaticalCase():
                        if "abl" in caseList:
                            caseList["abl"] = caseList["abl"] + 1
                        else:
                            caseList["abl"] = 1
                    if "acc" in argument.getGrammaticalCase():
                        if "acc" in caseList:
                            caseList["acc"] = caseList["acc"] + 1
                        else:
                            caseList["acc"] = 1
                    if "dat" in argument.getGrammaticalCase():
                        if "dat" in caseList:
                            caseList["dat"] = caseList["dat"] + 1
                        else:
                            caseList["dat"] = 1
                    if "gen" in argument.getGrammaticalCase():
                        if "gen" in caseList:
                            caseList["gen"] = caseList["gen"] + 1
                        else:
                            caseList["gen"] = 1
                    if "ins" in argument.getGrammaticalCase():
                        if "ins" in caseList:
                            caseList["ins"] = caseList["ins"] + 1
                        else:
                            caseList["ins"] = 1
                    if "loc" in argument.getGrammaticalCase():
                        if "loc" in caseList:
                            caseList["loc"] = caseList["loc"] + 1
                        else:
                            caseList["loc"] = 1
                    if "nom" in argument.getGrammaticalCase():
                        if "nom" in caseList:
                            caseList["nom"] = caseList["nom"] + 1
                        else:
                            caseList["nom"] = 1
        self.assertEqual(422, caseList["abl"])
        self.assertEqual(4690, caseList["acc"])
        self.assertEqual(2423, caseList["dat"])
        self.assertEqual(880, caseList["gen"])
        self.assertEqual(459, caseList["ins"])
        self.assertEqual(673, caseList["loc"])
        self.assertEqual(2069, caseList["nom"])

    def test_ArgName(self):
        nameList = {}
        for i in range(self.framesetList.size()):
            for argument in self.framesetList.getFrameSet(i).getFramesetArguments():
                if argument.getArgumentType() in nameList:
                    nameList[argument.getArgumentType()] = nameList[argument.getArgumentType()] + 1
                else:
                    nameList[argument.getArgumentType()] = 1
        self.assertEqual(14669, nameList["ARG0"])
        self.assertEqual(13127, nameList["ARG1"])
        self.assertEqual(1886, nameList["ARG2"])
        self.assertEqual(78, nameList["ARG3"])
        self.assertEqual(1, nameList["ARG4"])

    def test_ArgFunction(self):
        functionList = {}
        for i in range(self.framesetList.size()):
            for argument in self.framesetList.getFrameSet(i).getFramesetArguments():
                if argument.getFunction() in functionList:
                    functionList[argument.getFunction()] = functionList[argument.getFunction()] + 1
                else:
                    functionList[argument.getFunction()] = 1
        self.assertEqual(481, functionList["com"])
        self.assertEqual(14, functionList["ext"])
        self.assertEqual(814, functionList["loc"])
        self.assertEqual(198, functionList["rec"])
        self.assertEqual(14, functionList["pat"])
        self.assertEqual(10688, functionList["ppt"])
        self.assertEqual(605, functionList["src"])
        self.assertEqual(801, functionList["gol"])
        self.assertEqual(156, functionList["tmp"])
        self.assertEqual(14558, functionList["pag"])
        self.assertEqual(1432, functionList["dir"])

if __name__ == '__main__':
    unittest.main()
