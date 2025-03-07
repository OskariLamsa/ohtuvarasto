import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_tilavuus_alle_nolla(self):
        self.varasto2 = Varasto(-1)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)
    def test_konstruktori_saldo_alle_nolla(self):
        self.varasto3 = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto3.saldo, 0)
    def test_lisaa_negatiivi(self):
        self.varasto4 = Varasto(10)
        self.varasto4.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto4.saldo, 0)
    def test_lisaa_liikaa(self):
        self.varasto5 = Varasto(10)
        self.varasto5.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto5.saldo, 10)
    def test_ota_varastosta_negatiivi(self):
        self.varasto6 = Varasto(10, 5)
        self.varasto6.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto6.saldo, 5)
    def test_ota_varastosta_kaikki(self):
        self.varasto7 = Varasto(10, 5)
        self.assertAlmostEqual(self.varasto7.ota_varastosta(6), 5)
    def test_str(self):
        self.varasto8 = Varasto(10)
        self.assertAlmostEqual(str(self.varasto8), "saldo = 0, vielä tilaa 10")