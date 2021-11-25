import unittest

from PropBank.PredicateList import PredicateList


class PredicateListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.predicateList = PredicateList()

    def test_PredicateSize(self):
        self.assertEquals(8656, self.predicateList.size())

    def test_RoleSetSize(self):
        count = 0
        for lemma in self.predicateList.getLemmaList():
            count += self.predicateList.getPredicate(lemma).size()
        self.assertEquals(10685, count)

    def test_RoleSize(self):
        count = 0
        for lemma in self.predicateList.getLemmaList():
            for i in range(self.predicateList.getPredicate(lemma).size()):
                count += self.predicateList.getPredicate(lemma).getRoleSet(i).size()
        self.assertEquals(27080, count)

    def test_Function(self):
        functionList = {}
        for lemma in self.predicateList.getLemmaList():
            for i in range(self.predicateList.getPredicate(lemma).size()):
                for j in range(self.predicateList.getPredicate(lemma).getRoleSet(i).size()):
                    function = self.predicateList.getPredicate(lemma).getRoleSet(i).getRole(j).getF()
                    if function in functionList:
                        functionList[function] = functionList[function] + 1
                    else:
                        functionList[function] = 1
        self.assertEquals(197, functionList["com"])
        self.assertEquals(292, functionList["ext"])
        self.assertEquals(580, functionList["loc"])
        self.assertEquals(1104, functionList["prd"])
        self.assertEquals(2395, functionList["gol"])
        self.assertEquals(19, functionList["adj"])
        self.assertEquals(980, functionList["dir"])
        self.assertEquals(118, functionList["prp"])
        self.assertEquals(1007, functionList["mnr"])
        self.assertEquals(4, functionList["rec"])
        self.assertEquals(679, functionList["vsp"])
        self.assertEquals(14, functionList["adv"])
        self.assertEquals(10282, functionList["ppt"])
        self.assertEquals(267, functionList["cau"])
        self.assertEquals(37, functionList["tmp"])
        self.assertEquals(9105, functionList["pag"])

    def test_N(self):
        nList = {}
        for lemma in self.predicateList.getLemmaList():
            for i in range(self.predicateList.getPredicate(lemma).size()):
                for j in range(self.predicateList.getPredicate(lemma).getRoleSet(i).size()):
                    n = self.predicateList.getPredicate(lemma).getRoleSet(i).getRole(j).getN()
                    if n in nList:
                        nList[n] = nList[n] + 1
                    else:
                        nList[n] = 1
        self.assertEquals(8906, nList["0"])
        self.assertEquals(10375, nList["1"])
        self.assertEquals(5934, nList["2"])
        self.assertEquals(1313, nList["3"])
        self.assertEquals(417, nList["4"])
        self.assertEquals(57, nList["5"])
        self.assertEquals(6, nList["6"])
        self.assertEquals(72, nList["m"])


if __name__ == '__main__':
    unittest.main()
