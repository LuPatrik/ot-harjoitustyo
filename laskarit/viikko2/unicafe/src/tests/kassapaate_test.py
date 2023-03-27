import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate,None)

    def test_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_molempia_lounaita_nolla_myyty_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisostos_kasvattaa_oikealla_maaralla_kassapaatetta(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+240)

        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240+240)

    def test_maukas_kateisostos_kasvattaa_oikealla_maaralla_kassapaatetta(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+400)

        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400+400)

    def test_edullinen_kateisostos_antaa_oikean_maaran_vaihtorahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(340), 100)

    def test_maukas_kateisostos_antaa_oikean_maaran_vaihtorahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_myytyjen_lounaiden_maara_ei_kasva_kun_ei_ole_tarpeeksi_rahaa(self):

        self.kassapaate.syo_edullisesti_kateisella(0)
        self.kassapaate.syo_maukkaasti_kateisella(0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kaikki_rahat_palautetaan_kun_ei_ole_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100),100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(99),99)

    def test_korttimaksu_toimii_kun_on_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 3.60 euroa")
        
    def test_onnistunut_korttimaksu_kasvattaa_myytyja_lounaita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_epaonnistunut_korttimaksu_ei_kasvata_myytyja_lounaita(self):
        self.maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_epaonnistunut_korttimaksu_ei_kasvata_kassarahoja(self):
        self.maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_epaonnistunut_korttimaksu_palauttaa_falsen(self):
        self.maksukortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    
    def test_kortille_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)