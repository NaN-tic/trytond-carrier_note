#!/usr/bin/env python
# This file is part of the carrier_note module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_view, test_depends
import trytond.tests.test_tryton
import unittest


class CarrierNoteTestCase(unittest.TestCase):
    'Test Carrier Note module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('carrier_note')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('carrier_note')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CarrierNoteTestCase))
    return suite
