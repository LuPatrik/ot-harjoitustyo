import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):    
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 30.00 euroa")

    def test_saldo_ei_vahene_jos_ei_ole_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(9999)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldo_vahenee_jos_on_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")
    
    def test_riittaako_rahat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(9999), False)
        self.assertEqual(self.maksukortti.ota_rahaa(1), True)

