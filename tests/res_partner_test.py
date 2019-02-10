# -*- coding: utf-8 -*-

from odoo.tests import common

class TestResPartner(common.TransactionCase):




	def test_create_res_partner(self):
		# Create a new project with the test
		test_project = self.env['dreamsofft.hotel_config'].calcular_edad('2001/01/01')
		self.assertEquals(test_project, 18, "Converted quantity does not correspond.")
