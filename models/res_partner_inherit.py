# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services PVT. LTD.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# ---------------------------------------------------------------------------

import time
import datetime
from dateutil.relativedelta import relativedelta
import urllib2
from odoo.exceptions import except_orm, ValidationError
from odoo.tools import misc, DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT
from odoo import models, fields, api, _
from odoo import workflow
from decimal import Decimal
import logging
_logger = logging.getLogger(__name__)

class res_partner_inherit(models.Model):

	_name = 'res.partner'

	_inherit = 'res.partner'



		# Document information
	doctype = fields.Selection(
		[
			(11, "11 - Birth Certificate"),
			(12, "12 - Identity Card"),
			(13, "13 - Citizenship Card"),
			(21, "21 - Alien Registration Card"),
			(22, "22 - Foreigner ID"),
			(41, "41 - Passport"),
			(42, "42 - Foreign Identification Document")


		], "Type of Identification"
	)
	pais_del_ref_id = fields.Many2one('res.country', string='Pais de la identificacion')



	@api.onchange('company_type')
	def onChangeCompanyType(self):
		pass
