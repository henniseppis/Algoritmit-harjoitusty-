import unittest

from services.testi import Testi


class TestTesti(unittest.TestCase):
    def setUp(self):
        pass

    def test_testaa_testi(self):
        testi_vastaus = Testi.tulosta_moi(self)
        self.assertEqual(testi_vastaus,"moi")