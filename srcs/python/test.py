import unittest
from translator import main as execute


class TestTranslator(unittest.TestCase):

    def test_1111111(self):
        output = execute(['-t', 'hscs'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['hs', 'cs']. Actual: {output[1]}.")

    def test_1111110(self):
        output = execute(['-t', 'oscm'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['os', 'cm']. Actual: {output[1]}.")

    def test_1111101(self):
        output = execute(['-t', 'sbic'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['s', 'bi', 'c']. Actual: {output[1]}.")

    def test_1111100(self):
        output = execute(['-t', 'cnoq'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['c', 'no', 'q']. Actual: {output[1]}.")

    def test_1111011(self):
        output = execute(['-t', 'nirn'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ni', 'rn']. Actual: {output[1]}.")

    def test_1111010(self):
        output = execute(['-t', 'snam'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['sn', 'am']. Actual: {output[1]}.")

    def test_1111001(self):
        output = execute(['-t', 'csmf'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['c', 'sm', 'f']. Actual: {output[1]}.")

    def test_1111000(self):
        output = execute(['-t', 'nheg'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['n', 'he', 'g']. Actual: {output[1]}.")

    def test_1110111(self):
        output = execute(['-t', 'pbbh'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['pb', 'bh']. Actual: {output[1]}.")

    def test_1110110(self):
        output = execute(['-t', 'sbpm'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['sb', 'pm']. Actual: {output[1]}.")

    def test_1110101(self):
        output = execute(['-t', 'siik'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['si', 'i', 'k']. Actual: {output[1]}.")

    def test_1110100(self):
        output = execute(['-t', 'hokg'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['ho', 'k', 'g']. Actual: {output[1]}.")

    def test_1110011(self):
        output = execute(['-t', 'nilv'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ni', 'lv']. Actual: {output[1]}.")

    def test_1110010(self):
        output = execute(['-t', 'comt'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['co', 'mt']. Actual: {output[1]}.")

    def test_1110001(self):
        output = execute(['-t', 'nbln'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['nb', 'l', 'n']. Actual: {output[1]}.")

    def test_1110000(self):
        output = execute(['-t', 'cuxq'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['cu', 'x', 'q']. Actual: {output[1]}.")

    def test_1101111(self):
        output = execute(['-t', 'irhf'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ir', 'hf']. Actual: {output[1]}.")

    def test_1101110(self):
        output = execute(['-t', 'frna'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['fr', 'na']. Actual: {output[1]}.")

    def test_1101101(self):
        output = execute(['-t', 'srfb'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['s', 'rf', 'b']. Actual: {output[1]}.")

    def test_1101100(self):
        output = execute(['-t', 'ptcg'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['p', 'tc', 'g']. Actual: {output[1]}.")

    def test_1101011(self):
        output = execute(['-t', 'sres'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['sr', 'es']. Actual: {output[1]}.")

    def test_1101010(self):
        output = execute(['-t', 'ptam'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['pt', 'am']. Actual: {output[1]}.")

    def test_1101001(self):
        output = execute(['-t', 'pmdc'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['p', 'md', 'c']. Actual: {output[1]}.")

    def test_1101000(self):
        output = execute(['-t', 'cald'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['c', 'al', 'd']. Actual: {output[1]}.")

    def test_1100111(self):
        output = execute(['-t', 'sgyb'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['sg', 'yb']. Actual: {output[1]}.")

    def test_1100110(self):
        output = execute(['-t', 'krir'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['kr', 'ir']. Actual: {output[1]}.")

    def test_1100101(self):
        output = execute(['-t', 'ogko'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['og', 'k', 'o']. Actual: {output[1]}.")

    def test_1100100(self):
        output = execute(['-t', 'ogul'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['og', 'u', 'l']. Actual: {output[1]}.")

    def test_1100011(self):
        output = execute(['-t', 'irmc'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ir', 'mc']. Actual: {output[1]}.")

    def test_1100010(self):
        output = execute(['-t', 'srta'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['sr', 'ta']. Actual: {output[1]}.")

    def test_1100001(self):
        output = execute(['-t', 'ptju'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['pt', 'j', 'u']. Actual: {output[1]}.")

    def test_1100000(self):
        output = execute(['-t', 'clgj'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['cl', 'g', 'j']. Actual: {output[1]}.")

    def test_1011111(self):
        output = execute(['-t', 'fscu'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['f', 's', 'cu']. Actual: {output[1]}.")

    def test_1011110(self):
        output = execute(['-t', 'hybe'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['h', 'y', 'be']. Actual: {output[1]}.")

    def test_1011101(self):
        output = execute(['-t', 'bpus'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['b', 'pu', 's']. Actual: {output[1]}.")

    def test_1011100(self):
        output = execute(['-t', 'sscq'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['s', 'sc', 'q']. Actual: {output[1]}.")

    def test_1011011(self):
        output = execute(['-t', 'virn'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['v', 'i', 'rn']. Actual: {output[1]}.")

    def test_1011010(self):
        output = execute(['-t', 'okrg'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['o', 'k', 'rg']. Actual: {output[1]}.")

    def test_1011001(self):
        output = execute(['-t', 'ysgb'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['y', 'sg', 'b']. Actual: {output[1]}.")

    def test_1011000(self):
        output = execute(['-t', 'ksed'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['k', 'se', 'd']. Actual: {output[1]}.")

    def test_1010111(self):
        output = execute(['-t', 'kwbh'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['k', 'w', 'bh']. Actual: {output[1]}.")

    def test_1010110(self):
        output = execute(['-t', 'hvba'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['h', 'v', 'ba']. Actual: {output[1]}.")

    def test_1010101(self):
        output = execute(['-t', 'bswi'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['b', 's', 'w', 'i']. Actual: {output[1]}.")

    def test_1010100(self):
        output = execute(['-t', 'wynl'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['w', 'y', 'n', 'l']. Actual: {output[1]}.")

    def test_1010011(self):
        output = execute(['-t', 'wieu'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['w', 'i', 'eu']. Actual: {output[1]}.")

    def test_1010010(self):
        output = execute(['-t', 'bvge'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['b', 'v', 'ge']. Actual: {output[1]}.")

    def test_1010001(self):
        output = execute(['-t', 'fsai'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['f', 's', 'a', 'i']. Actual: {output[1]}.")

    def test_1010000(self):
        output = execute(['-t', 'wkml'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['w', 'k', 'm', 'l']. Actual: {output[1]}.")

    def test_1001111(self):
        output = execute(['-t', 'oasn'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['o', 'as', 'n']. Actual: {output[1]}.")

    def test_1001110(self):
        output = execute(['-t', 'itsg'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['i', 't', 'sg']. Actual: {output[1]}.")

    def test_1001101(self):
        output = execute(['-t', 'sdby'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['s', 'db', 'y']. Actual: {output[1]}.")

    def test_1001100(self):
        output = execute(['-t', 'orbg'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['o', 'rb', 'g']. Actual: {output[1]}.")

    def test_1001011(self):
        output = execute(['-t', 'hmtb'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['h', 'mt', 'b']. Actual: {output[1]}.")

    def test_1001010(self):
        output = execute(['-t', 'orgd'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['o', 'r', 'gd']. Actual: {output[1]}.")

    def test_1001001(self):
        output = execute(['-t', 'utly'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['u', 'tl', 'y']. Actual: {output[1]}.")

    def test_1001000(self):
        output = execute(['-t', 'hmdj'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['h', 'md', 'j']. Actual: {output[1]}.")

    def test_1000111(self):
        output = execute(['-t', 'ujbi'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['u', 'j', 'bi']. Actual: {output[1]}.")

    def test_1000110(self):
        output = execute(['-t', 'kmsr'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['k', 'm', 'sr']. Actual: {output[1]}.")

    def test_1000101(self):
        output = execute(['-t', 'kqko'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['k', 'q', 'k', 'o']. Actual: {output[1]}.")

    def test_1000100(self):
        output = execute(['-t', 'kjsa'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['k', 'j', 's', 'a']. Actual: {output[1]}.")

    def test_1000011(self):
        output = execute(['-t', 'keas'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['k', 'e', 'as']. Actual: {output[1]}.")

    def test_1000010(self):
        output = execute(['-t', 'ygge'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['y', 'g', 'ge']. Actual: {output[1]}.")

    def test_1000001(self):
        output = execute(['-t', 'kmay'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['k', 'm', 'a', 'y']. Actual: {output[1]}.")

    def test_1000000(self):
        output = execute(['-t', 'urtt'])[0]
        self.assertIs(int(output[0]), int(3), f"Expected: ['u', 'r', 't', 't']. Actual: {output[1]}.")

    def test_0111111(self):
        output = execute(['-t', 'mcni'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['mc', 'ni']. Actual: {output[1]}.")

    def test_0111110(self):
        output = execute(['-t', 'dsne'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ds', 'ne']. Actual: {output[1]}.")

    def test_0111101(self):
        output = execute(['-t', 'tsck'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ts', 'c', 'k']. Actual: {output[1]}.")

    def test_0111100(self):
        output = execute(['-t', 'tcnj'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['tc', 'n', 'j']. Actual: {output[1]}.")

    def test_0111011(self):
        output = execute(['-t', 'acli'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ac', 'li']. Actual: {output[1]}.")

    def test_0111010(self):
        output = execute(['-t', 'tcar'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['tc', 'ar']. Actual: {output[1]}.")

    def test_0111001(self):
        output = execute(['-t', 'liry'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['l', 'ir', 'y']. Actual: {output[1]}.")

    def test_0111000(self):
        output = execute(['-t', 'dbeg'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['d', 'be', 'g']. Actual: {output[1]}.")

    def test_0110111(self):
        output = execute(['-t', 'rnnb'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['rn', 'nb']. Actual: {output[1]}.")

    def test_0110110(self):
        output = execute(['-t', 'eukr'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['eu', 'kr']. Actual: {output[1]}.")

    def test_0110101(self):
        output = execute(['-t', 'mnsu'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['mn', 's', 'u']. Actual: {output[1]}.")

    def test_0110100(self):
        output = execute(['-t', 'auvd'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['au', 'v', 'd']. Actual: {output[1]}.")

    def test_0110011(self):
        output = execute(['-t', 'aslu'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['as', 'lu']. Actual: {output[1]}.")

    def test_0110010(self):
        output = execute(['-t', 'rbmg'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['rb', 'mg']. Actual: {output[1]}.")

    def test_0110001(self):
        output = execute(['-t', 'dyqk'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['dy', 'q', 'k']. Actual: {output[1]}.")

    def test_0110000(self):
        output = execute(['-t', 'acxl'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['ac', 'x', 'l']. Actual: {output[1]}.")

    def test_0101111(self):
        output = execute(['-t', 'tacn'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ta', 'cn']. Actual: {output[1]}.")

    def test_0101110(self):
        output = execute(['-t', 'mtba'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['mt', 'ba']. Actual: {output[1]}.")

    def test_0101101(self):
        output = execute(['-t', 'xesu'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['xe', 's', 'u']. Actual: {output[1]}.")

    def test_0101100(self):
        output = execute(['-t', 'athl'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['at', 'h', 'l']. Actual: {output[1]}.")

    def test_0101011(self):
        output = execute(['-t', 'ramc'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ra', 'mc']. Actual: {output[1]}.")

    def test_0101010(self):
        output = execute(['-t', 'erar'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['er', 'ar']. Actual: {output[1]}.")

    def test_0101001(self):
        output = execute(['-t', 'atlw'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['a', 'tl', 'w']. Actual: {output[1]}.")

    def test_0101000(self):
        output = execute(['-t', 'gatt'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['g', 'at', 't']. Actual: {output[1]}.")

    def test_0100111(self):
        output = execute(['-t', 'genh'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ge', 'nh']. Actual: {output[1]}.")

    def test_0100110(self):
        output = execute(['-t', 'tmkr'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['tm', 'kr']. Actual: {output[1]}.")

    def test_0100101(self):
        output = execute(['-t', 'agww'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ag', 'w', 'w']. Actual: {output[1]}.")

    def test_0100100(self):
        output = execute(['-t', 'atnm'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['at', 'n', 'm']. Actual: {output[1]}.")

    def test_0100011(self):
        output = execute(['-t', 'mdrb'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['md', 'rb']. Actual: {output[1]}.")

    def test_0100010(self):
        output = execute(['-t', 'gaal'])[0]
        self.assertIs(int(output[0]), int(0), f"Expected: ['ga', 'al']. Actual: {output[1]}.")

    def test_0100001(self):
        output = execute(['-t', 'arjc'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['ar', 'j', 'c']. Actual: {output[1]}.")

    def test_0100000(self):
        output = execute(['-t', 'arlq'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['ar', 'l', 'q']. Actual: {output[1]}.")

    def test_0011111(self):
        output = execute(['-t', 'xnbi'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['x', 'n', 'bi']. Actual: {output[1]}.")

    def test_0011110(self):
        output = execute(['-t', 'xosm'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['x', 'o', 'sm']. Actual: {output[1]}.")

    def test_0011101(self):
        output = execute(['-t', 'qpbb'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['q', 'pb', 'b']. Actual: {output[1]}.")

    def test_0011100(self):
        output = execute(['-t', 'qcox'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['q', 'co', 'x']. Actual: {output[1]}.")

    def test_0011011(self):
        output = execute(['-t', 'apti'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['a', 'p', 'ti']. Actual: {output[1]}.")

    def test_0011010(self):
        output = execute(['-t', 'gpam'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['g', 'p', 'am']. Actual: {output[1]}.")

    def test_0011001(self):
        output = execute(['-t', 'lsrw'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['l', 'sr', 'w']. Actual: {output[1]}.")

    def test_0011000(self):
        output = execute(['-t', 'qcad'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['q', 'ca', 'd']. Actual: {output[1]}.")

    def test_0010111(self):
        output = execute(['-t', 'jpco'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['j', 'p', 'co']. Actual: {output[1]}.")

    def test_0010110(self):
        output = execute(['-t', 'ayog'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['a', 'y', 'og']. Actual: {output[1]}.")

    def test_0010101(self):
        output = execute(['-t', 'afuc'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['a', 'f', 'u', 'c']. Actual: {output[1]}.")

    def test_0010100(self):
        output = execute(['-t', 'xvng'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['x', 'v', 'n', 'g']. Actual: {output[1]}.")

    def test_0010011(self):
        output = execute(['-t', 'ahdy'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['a', 'h', 'dy']. Actual: {output[1]}.")

    def test_0010010(self):
        output = execute(['-t', 'gitm'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['g', 'i', 'tm']. Actual: {output[1]}.")

    def test_0010001(self):
        output = execute(['-t', 'lnji'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['l', 'n', 'j', 'i']. Actual: {output[1]}.")

    def test_0010000(self):
        output = execute(['-t', 'muqd'])[0]
        self.assertIs(int(output[0]), int(3), f"Expected: ['m', 'u', 'q', 'd']. Actual: {output[1]}.")

    def test_0001111(self):
        output = execute(['-t', 'edsb'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['e', 'ds', 'b']. Actual: {output[1]}.")

    def test_0001110(self):
        output = execute(['-t', 'qmog'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['q', 'm', 'og']. Actual: {output[1]}.")

    def test_0001101(self):
        output = execute(['-t', 'qaup'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['q', 'au', 'p']. Actual: {output[1]}.")

    def test_0001100(self):
        output = execute(['-t', 'xlur'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['x', 'lu', 'r']. Actual: {output[1]}.")

    def test_0001011(self):
        output = execute(['-t', 'rlrh'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['r', 'lr', 'h']. Actual: {output[1]}.")

    def test_0001010(self):
        output = execute(['-t', 'dgal'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['d', 'g', 'al']. Actual: {output[1]}.")

    def test_0001001(self):
        output = execute(['-t', 'eeri'])[0]
        self.assertIs(int(output[0]), int(1), f"Expected: ['e', 'er', 'i']. Actual: {output[1]}.")

    def test_0001000(self):
        output = execute(['-t', 'qrem'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['q', 're', 'm']. Actual: {output[1]}.")

    def test_0000111(self):
        output = execute(['-t', 'lxnh'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['l', 'x', 'nh']. Actual: {output[1]}.")

    def test_0000110(self):
        output = execute(['-t', 'dlna'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['d', 'l', 'na']. Actual: {output[1]}.")

    def test_0000101(self):
        output = execute(['-t', 'gtfk'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['g', 't', 'f', 'k']. Actual: {output[1]}.")

    def test_0000100(self):
        output = execute(['-t', 'qgkq'])[0]
        self.assertIs(int(output[0]), int(3), f"Expected: ['q', 'g', 'k', 'q']. Actual: {output[1]}.")

    def test_0000011(self):
        output = execute(['-t', 'qgts'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['q', 'g', 'ts']. Actual: {output[1]}.")

    def test_0000010(self):
        output = execute(['-t', 'gjrg'])[0]
        self.assertIs(int(output[0]), int(2), f"Expected: ['g', 'j', 'rg']. Actual: {output[1]}.")

    def test_0000001(self):
        output = execute(['-t', 'tjay'])[0]
        self.assertIs(int(output[0]), int(3), f"Expected: ['t', 'j', 'a', 'y']. Actual: {output[1]}.")

    def test_0000000(self):
        output = execute(['-t', 'eqae'])[0]
        self.assertIs(int(output[0]), int(4), f"Expected: ['e', 'q', 'a', 'e']. Actual: {output[1]}.")

if __name__ == '__main__':
    unittest.main()
