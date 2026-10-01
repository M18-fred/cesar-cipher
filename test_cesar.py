import unittest
from cesar import chiffrer, dechiffrer

class TestCesar(unittest.TestCase):

    def test_chiffrer_simple(self):
        resultat = chiffrer("ABC", 1)
        self.assertEqual(resultat, "BCD")

    def test_dechiffrer_simple(self):
        resultat = dechiffrer("BCD",1)
        self.assertEqual(resultat,"ABC")

    def test_chiffrer_avec_espaces_et_ponctuation(self):
        resultat = chiffrer("Hello, World!", 3)
        self.assertEqual(resultat, "Khoor, Zruog!")

    def test_cle_26_ne_change_rien(self):
        texte = "Hello World!"
        resultat = chiffrer(texte, 26)
        self.assertEqual(resultat, texte)

if __name__ == "__main__":
    unittest.main()