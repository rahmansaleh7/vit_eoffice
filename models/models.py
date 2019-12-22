# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

SURAT_STATES =[('draft','Draft'),('needapproval','Need Approval'),
				('unread','Approved'),('read','Read')]

class Surat(models.Model):
	_name = 'vit_eoffice.surat'

	name = fields.Char(string="No Surat", required=False, )
	perihal = fields.Char(string="Perihal", required=False, )
	tanggal = fields.Date(string="Tanggal", required=True, )
	dari	= fields.Many2one(comodel_name="res.users",
							string="Dari", 
							required=True, )
	klasifikasisurat = fields.Many2one(comodel_name="vit_eoffice.klasifikasisurat",
									string="Klasifikasi Surat", 
									required=True, )
	templatesurat = fields.Many2one(comodel_name="vit_eoffice.templatesurat",
									string="Template Surat", 
									required=True, )
	isisurat = fields.Text(string="Isi Surat", )
	history = fields.Char(string="History", )
	# kepada = fields.One2many(comodel_name="res.users",
	# 						inverse_name="res.users",
	# 						required=False,
	# 						ondelete="cascade", )
	# tembusan = fields.One2many(comodel_name="vit_eoffice.user",
	# 							inverse_name="id_user",
	# 							required=False,
	# 							ondelete="cascade", )

	state = fields.Selection(string="Status", 
							selection=SURAT_STATES,
							required=True,
							readonly=True,
							default=SURAT_STATES[0][0])

	# class Replysurat(models.Model):
	# 	_name = 'vit_eoffice.replysurat'

	# 	name = fields.Char(string="No Surat", required=False, )
	# 	Perihal = fields.Char(string="Perihal", required=True, )
	# 	tanggal = fields.Date(string="Tanggal", required=True, )
	# 	dari	= fields.Many2one(comodel_name="res.users",
	# 							string="Dari", 
	# 							required=True, )
	# 	klasifikasisurat = fields.Many2one(comodel_name="vit_eoffice.klasifikasisurat",
	# 									string="Klasifikasi Surat", 
	# 									required=True, )
	# 	templatesurat = fields.Many2one(comodel_name="vit_eoffice.templatesurat",
	# 									string="Template Surat", 
	# 									required=True, )
	# 	isisurat = fields.Text(string="Isi Surat", )
	# 	history = fields.Char(string="History", )
	# 	kepada = fields.One2many(comodel_name="vit_eoffice.user",
	# 							inverse_name="name",
	# 							required=False,
	# 							ondelete="cascade", )
	# 	tembusan = fields.One2many(comodel_name="vit_eoffice.user",
	# 								inverse_name="name",
	# 								required=False,
	# 								ondelete="cascade", )
	# 	sumbersurat = fields.Many2one(comodel_name="vit_eoffice.surat",
	# 								required=True, )

	# 	state = fields.Selection(string="Status", 
	# 							selection=SURAT_STATES,
	# 							required=True,
	# 							readonly=True,
	# 							default=SURAT_STATES[0][0])

	@api.multi
	def action_draft(self):
		self.state = SURAT_STATES[0][0]
	@api.multi
	def action_needapproval(self):
		self.state = SURAT_STATES[1][0]
	@api.multi
	def action_unread(self):
		self.state = SURAT_STATES[2][0]
	@api.multi
	def action_read(self):
		self.state = SURAT_STATES[3][0]

	@api.model
	def create(self, vals):
		if not vals.get('name', False) or vals['name'] == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('vit_eoffice.surat') or 'Error Number!!!'
		return super(Surat, self).create(vals)


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