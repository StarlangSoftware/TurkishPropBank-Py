import unittest

from PropBank.PredicateList import PredicateList


class PredicateListTest(unittest.TestCase):

    def setUp(self) -> None:
        self.predicateList = PredicateList()

    def test_PredicateSize(self):
        self.assertEqual(8656, self.predicateList.size())

    def test_RoleSetSize(self):
        count = 0
        for lemma in self.predicateList.getLemmaList():
            count += self.predicateList.getPredicate(lemma).size()
        self.assertEqual(10685, count)

    def test_RoleSize(self):
        count = 0
        for lemma in self.predicateList.getLemmaList():
            for i in range(self.predicateList.getPredicate(lemma).size()):
                count += self.predicateList.getPredicate(lemma).getRoleSet(i).size()
        self.assertEqual(27080, count)

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
        self.assertEqual(197, functionList["com"])
        self.assertEqual(292, functionList["ext"])
        self.assertEqual(580, functionList["loc"])
        self.assertEqual(1104, functionList["prd"])
        self.assertEqual(2395, functionList["gol"])
        self.assertEqual(19, functionList["adj"])
        self.assertEqual(980, functionList["dir"])
        self.assertEqual(118, functionList["prp"])
        self.assertEqual(1007, functionList["mnr"])
        self.assertEqual(4, functionList["rec"])
        self.assertEqual(679, functionList["vsp"])
        self.assertEqual(14, functionList["adv"])
        self.assertEqual(10282, functionList["ppt"])
        self.assertEqual(267, functionList["cau"])
        self.assertEqual(37, functionList["tmp"])
        self.assertEqual(9105, functionList["pag"])

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
        self.assertEqual(8906, nList["0"])
        self.assertEqual(10375, nList["1"])
        self.assertEqual(5934, nList["2"])
        self.assertEqual(1313, nList["3"])
        self.assertEqual(417, nList["4"])
        self.assertEqual(57, nList["5"])
        self.assertEqual(6, nList["6"])
        self.assertEqual(72, nList["m"])


if __name__ == '__main__':
    unittest.main()
