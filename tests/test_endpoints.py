from __future__ import print_function, unicode_literals
from unittest import TestCase
from tx_manager.tx_manager import TxManager


class TestEndpoints(TestCase):

    def test_endpoints(self):
        manager = TxManager()

        # test the default constructor
        self.assertFalse(manager.api_url)

        # test getting the whole list
        langs = Language.load_languages()
        self.assertGreater(len(langs), 7000)

        # get the first item (as of 29 AUG 2016)
        lang_aa = [x for x in langs if x.lc == 'aa'][0]
        self.assertIsNotNone(lang_aa)
        self.assertEqual('Afar', lang_aa.ang)

        # get the last item (as of 29 AUG 2016)
        lang_zzj = [x for x in langs if x.lc == 'zzj'][0]
        self.assertIsNotNone(lang_zzj)
        self.assertEqual('Zhuang, Zuojiang', lang_zzj.ang)

        # get English
        lang_en = [x for x in langs if x.lc == 'en'][0]
        self.assertIsNotNone(lang_en)
        self.assertEqual('English', lang_en.ang)
