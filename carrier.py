# This file is part of the carrier_note module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Carrier']
__metaclass__ = PoolMeta


class Carrier:
    __name__ = 'carrier'
    note = fields.Text('Note')