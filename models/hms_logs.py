from odoo import models, fields

class Logs(models.Model):
    _name = 'hms.logs'

    description=fields.Char()
    patient_id=fields.Many2one(comodel_name="hms.patient")
    _columns = {
        'create_date': fields.Datetime('Date Created', readonly=True),
        'create_uid': fields.Many2one('res.users', 'by User', readonly=True),
        }
