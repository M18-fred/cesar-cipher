import unittest
from cesar import chiffrer
from cryptanalyse import deviner_cle

class TestCryptanalyse(unittest.TestCase):

    def test_deviner_cle_texte_long(self):
        texte_original = "Le chiffrement de Cesar est une methode de cryptographie tres ancienne utilisee depuis l antiquite"
        texte_chiffre = chiffrer(texte_original, 7)
        cle_devinee = deviner_cle(texte_chiffre)
        self.assertEqual(cle_devinee, 7)

if __name__ == "__main__":
    unittest.main()