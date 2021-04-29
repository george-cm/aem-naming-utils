import pytest
from aem_naming_utils import AemNamingUtils

class TestClassCreateProperFileName:

    @pytest.mark.parametrize(
        "instr, outstr",
        [
            ('filename--with--multiple--hypens', 'filename-with-multiple-hypens'),
            ('multiple  spaces', 'multiple-spaces'),
            ('extra space at the end ', 'extra-space-at-the-end'),
            (' extra space at the beginning', 'extra-space-at-the-beginning'),
            ('extra hypen at end-', 'extra-hypen-at-end'),
            ('-extra hyphen at begining', 'extra-hyphen-at-begining'),
            ('-extra hyphen at begining and end-', 'extra-hyphen-at-begining-and-end'),
            ('----extra hyphens at begining and end--', 'extra-hyphens-at-begining-and-end'),
            ('one_underscore', 'one-underscore'),
            ('multiple___underscores', 'multiple-underscores'),
            ('underscore at end_', 'underscore-at-end'),
            ('_underscore at beginnning', 'underscore-at-beginnning'),
            ('_underscore at beginnning and end_', 'underscore-at-beginnning-and-end'),
            ('awesome   filename with extention.PDF____   -----', 'awesome-filename-with-extention.pdf'),
            ('__  ---- %@#@ ^^^!@#$*() awesome   filename with extention.PDF____   -----', 'awesome-filename-with-extention.pdf'),
            ('__  \'---- "" %@#@ nothing^^^!@#$*(somehting) awesome   filename with extention.PDF____   -----', 'nothing-somehting-awesome-filename-with-extention.pdf'),
            ('__  ---- %@#@ 1.3 nothing^^^!@#$*(somehting) awesome   filename with extention.PDF____   -----', '1-3-nothing-somehting-awesome-filename-with-extention.pdf'),
            ('filename ™ with trademark ™', 'filename-with-trademark'),
            ('filename ® with copyright ® ', 'filename-with-copyright'),
            ('filename with single quote \' in it', 'filename-with-single-quote-in-it'),
            ('filename with double quote \" in it', 'filename-with-double-quote-in-it'),
        ]
    )

    def test_create_proper_name(self, instr, outstr):
        anu = AemNamingUtils()
        name = anu.create_proper_name(instr)
        assert name == outstr


class TestCreateProperUrl:

    @pytest.mark.parametrize(
        'prefix, product_name, product_primary_category, url', 
        [
            ("https://sps.honeywell.com/us/en/products", "T Handle Adapter", "AEM-SFT-3004 - Safety-->Electrical Safety-->Grounding Equipment", "https://sps.honeywell.com/us/en/products/safety/electrical-safety/grounding-equipment/t-handle-adapter"),
            ("https://sps.honeywell.com/us/en/products", "1-inch Series", "DSIT-01100 - Sensing & IOT-->Sensors-->Motion & Position Sensors-->Resolvers", "https://sps.honeywell.com/us/en/products/sensing-and-iot/sensors/motion-and-position-sensors/resolvers/1-inch-series"),
            ("https://sps.honeywell.com/us/en/products", "Voyager 1200g General Duty Scanner", "IPH00108 - Productivity-->Barcode Scanners-->General Purpose Handheld", "https://sps.honeywell.com/us/en/products/productivity/barcode-scanners/general-purpose-handheld/voyager-1200g-general-duty-scanner"),
            ("https://sps.honeywell.com/mx/es/products", "Voyager 1200g General Duty Scanner", "IPH00108 - Productivity-->Barcode Scanners-->General Purpose Handheld", "https://sps.honeywell.com/mx/es/products/productivity/barcode-scanners/general-purpose-handheld/voyager-1200g-general-duty-scanner"),
        ])

    def test_create_proper_url(self, prefix, product_name, product_primary_category, url):
        anu = AemNamingUtils()
        proper_url = anu.create_proper_url(prefix, product_name, product_primary_category)
        assert proper_url == url