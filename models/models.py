# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Surat(models.Model):
	_name = 'vit_eoffice.surat'

	nosurat = fields.Char(string="No Surat", required=True, )
	name = fields.Char(string="Perihal", required=True, )
	tanggal = fields.Date(string="Tanggal", required=True, )
	dari	= fields.Char(string="Dari", required=True, )
	klasifikasisurat = fields.Many2one(comodel_name="vit_eoffice.klasifikasisurat",
									string="Klasifikasi Surat", 
									required="True")
	templatesurat = fields.Many2one(comodel_name="vit_eoffice.templatesurat",
									string="Template Surat", 
									required="True")
	isisurat = fields.Text(string="Isi Surat", )
	history = fields.Char(string="History", )


class Klasifikasisurat(models.Model):
	_name ='vit_eoffice.klasifikasisurat'

	kodesurat = fields.Char(string="Kode Surat", required=True, )
	name = fields.Char(string="Nama", required=True, )


class Templatesurat(models.Model):
	_name = 'vit_eoffice.templatesurat'

	kodetemp = fields.Char(string="Kode", required=True, )
	name = fields.Char(string="Nama", required=True, )
	tempsurat = fields.Text(string="Template Surat", )


























# class vit_eoffice(models.Model):
#     _name = 'vit_eoffice.vit_eoffice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100