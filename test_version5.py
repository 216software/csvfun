# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

import csv
import tempfile
import unittest

import version5

class TestHouseDetector(unittest.TestCase):

    def setUp(self):

        self.bogus_out_csv_thingy = csv.DictWriter(
            tempfile.TemporaryFile(mode="w"),
            ["street address", "status", "rounded price"])

        self.good_house_data = {
            "price": 100 * 1000,
            "sourceStatus": "Active",
            "street": "742 Evergreen Terrace"}

        self.bad_house_data = {
            "price": 1000 * 1000,
            "sourceStatus": "Active",
            "street": "742 Evergreen Terrace"}

    def test_bad_house(self):

        self.assertIsNone(
            version5.handle_house_row(
                self.bogus_out_csv_thingy,
                self.bad_house_data))

    def test_good_house(self):

        self.assertTrue(
            version5.handle_house_row(
                self.bogus_out_csv_thingy,
                self.good_house_data))


if __name__ == "__main__":
    unittest.main()
