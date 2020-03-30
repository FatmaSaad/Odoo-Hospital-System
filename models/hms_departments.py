from odoo import models, fields

class Department(models.Model):
    _name = 'hms.department'

    name=fields.Char()
    Num_of_Beds=fields.Integer()
    is_open=fields.Boolean()
    patients=fields.One2many(comodel_name="hms.patient",inverse_name="department_id")
