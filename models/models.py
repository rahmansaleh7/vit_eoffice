# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

SURAT_STATES =[('draft','Draft'),('needapproval','Need Approval'),
				('unread','Approved'),('read','Read')]

class Surat(models.Model):
	_name = 'vit_eoffice.surat'

	name = fields.Char(string="No Surat", required=False, )
	perihal = fields.Char(string="Perihal", required=True, )
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
	kepada = fields.One2many(comodel_name="vit_eoffice.kepada", 
									inverse_name="doc_id", 
									string="Kepada", 
									ondelete="cascade", 
									states={'draft': [('readonly', False)]})
	tembusan = fields.One2many(comodel_name="vit_eoffice.tembusan", 
								inverse_name="doc_id", 
								string="Tembusan", 
								ondelete="cascade", 
								states={'draft': [('readonly', False)]})
	sumbersurat = fields.Many2one(comodel_name="vit_eoffice.surat", 
								string="Sumber Surat")
	state = fields.Selection(string="Status", 
							selection=SURAT_STATES,
							required=True,
							readonly=True,
							default=SURAT_STATES[0][0])

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


	@api.multi        
	def action_reply(self,cr,uid,ids,context=None):
		
		######################################################################
		# Mengambil Surat Lama
		######################################################################
		data = self.browse(cr, uid, ids, [])[0]

		######################################################################
		# set defautl values for the redirect 
		######################################################################
		context.update({
			'default_parent_id' : data.id,
			'default_user_id'   : uid,
			'default_to_user_ids' : [(0, 0, {'user_id': data.user_id.id })]
		})

		######################################################################
		# history 
		######################################################################
		self.insert_history(cr, uid, ids[0], 'Replied')

		######################################################################
		# return and show the view  
		######################################################################
		return {
			'name': _('Reply Surat'),
			'view_type': 'form',
			"view_mode": 'form',
			'res_model': 'vit_eoffice.surat',
			'type': 'ir.actions.act_window',
			'context': context,
		}


class Klasifikasisurat(models.Model):
	_name ='vit_eoffice.klasifikasisurat'

	kodesurat = fields.Char(string="Kode Surat", required=True, )
	name = fields.Char(string="Nama", required=True, )


class Templatesurat(models.Model):
	_name = 'vit_eoffice.templatesurat'

	kodetemp = fields.Char(string="Kode", required=True, )
	name = fields.Char(string="Nama", required=True, )
	tempsurat = fields.Text(string="Template Surat", )


class to_user(models.Model):
	_name = 'vit_eoffice.kepada'
	_rec_name = 'user_id'
	
	user_id = fields.Many2one(comodel_name="res.users", 
								string="User")
	doc_id = fields.Many2one(comodel_name="vit_eoffice.surat", 
								string="Surat")
	read_status = fields.Boolean(string="Read",
								readonly=True, )
	

class cc_user(models.Model):
	_name = 'vit_eoffice.tembusan'
	_rec_name = 'user_id'
	
	user_id = fields.Many2one(comodel_name="res.users", 
								string="User")
	doc_id = fields.Many2one(comodel_name="vit_eoffice.surat", 
								string="Surat")
	read_status = fields.Boolean(string="Read",
								readonly=True, )
