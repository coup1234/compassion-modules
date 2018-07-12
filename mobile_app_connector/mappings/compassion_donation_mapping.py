# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Compassion CH (http://www.compassion.ch)
#    Releasing children from poverty in Jesus' name
#    @author: Emanuel Cino <ecino@compassion.ch>
#
#    The licence is in the file __manifest__.py
#
##############################################################################
from odoo.addons.message_center_compassion.mappings.base_mapping import \
    OnrampMapping


class MobileDonationMapping(OnrampMapping):
    ODOO_MODEL = 'product.template'
    MAPPING_NAME = 'mobile_app_donation'

    CONNECT_MAPPING = {
    "DisplayOrder": "id",
    "FundName":"name",
    "Id": "id"
    }

    FIELDS_TO_SUBMIT = {k: None for k, v in CONNECT_MAPPING.iteritems() if v}
