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
			(31, "31 - NIT"),
			(41, "41 - Passport"),
			(42, "42 - Foreign Identification Document")


		],"Type of Identification",default=13
	)
	pais_del_ref_id = fields.Many2one('res.country',string='Nacionalidad')
	

	departamento_del_ref_id =fields.Many2one('res.country.state', string='Departamento')
	
	ciudad_del_ref_id =fields.Many2one('res.country.state.city', string='Ciudad')

	transporte = fields.Selection(
		[
			(1, "Aereo"),
			(2, "Terrestre"),
			(3, "Otros")
		], "Tipo de transporte"
	)
	
	tipo_transporte = fields.Selection(
		[
			(1, "Publico"),
			(2, "Particular")

		], "Tipo de vehiculo"
	)
	
	placa = fields.Char('placa', size=10)
	
	reserva = fields.Selection(
		[
			(1, "Web Finca Hotel"),
			(2, "Central de reserva"),
			(3, "Hotel"),
			(4, "Agencia de viajes"),
			(5, "Otros")
		], "Tipo de reserva"
	)

	autorizacion = fields.Selection(
		[
			(1, "Si"),
			(2, "No")
		], "Autorizacion correo electronico"
	)

	@api.onchange('company_type')
	def onChangeCompanyType(self):
		pass

	@api.onchange()
	def onchange_location(self, cr, uid):
		pass
	
	@api.onchange('pais_del_ref_id')
	def _onchange_country_id(self):
		if self.pais_del_ref_id:
			return {'domain': {'departamento_del_ref_id': [('country_id', '=', self.pais_del_ref_id.id)]}}
		else:
			return {'domain': {'departamento_del_ref_id': []}}


	@api.onchange('departamento_del_ref_id')
	def _onchange_departamento_id(self):
		if self.departamento_del_ref_id:
			return {'domain': {'ciudad_del_ref_id': [('state_id', '=', self.departamento_del_ref_id.id)]}}
		else:
			return {'domain': {'ciudad_del_ref_id': []}}


	@api.onchange('x_name1', 'x_name2', 'x_lastname1', 'x_lastname2', 'companyName',
				'pos_name', 'companyBrandName')
	def _concat_name(self):
		"""
	Este es el metodo para que deje que se pueda crear nombres con ñ y con tilde
		"""
		
		if self.x_name1 is False:
			self.x_name1 = ''

		if self.x_name2 is False:
			self.x_name2 = ''

		if self.x_lastname1 is False:
			self.x_lastname1 = ''

		if self.x_lastname2 is False:
			self.x_lastname2 = ''


		

		nameList = [
			self.x_name1,
			self.x_name2,
			self.x_lastname1,
			self.x_lastname2
		]

		formatedList = []
		if self.companyName is False:
			if self.type == 'delivery':
				self.name = self.pos_name
				self.x_name1 = False
				self.x_name2 = False
				self.x_lastname1 = False
				self.x_lastname2 = False
				self.doctype = 1
			else:
				
				for item in nameList:
				
					if item is not '':
						formatedList.append(item)
				self.name = ' ' .join(formatedList).title()
		else:
			
			
			if self.companyBrandName is not False:
				delimiter = ', '
				company_list = (self.companyBrandName, self.companyName)
				self.name = delimiter.join(company_list).title()
			else:
				self.name = self.companyName.title()

	
	
	
	
	

