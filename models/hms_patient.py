from odoo import models, fields, api

import time

class hms_patient(models.Model):
    _name = "hms.patient"
    _rec_name = 'fname'


    fname=fields.Char()
    lname=fields.Char()
    birth_date=fields.Date()
    history=fields.Html()
    CR_ratio=fields.Float()
    blood_type=fields.Selection([('A+','A+'),
                                 ('A-','A-'),
                                 ('B+', 'B+'),
                                 ('B-', 'B-'),
                                 ('AB+','AB+'),
                                 ('AB-','AB-'),
                                 ('O+','O+'),
                                 ('O-', 'O-')
                                 ],
                                default="A+")
    PCR=fields.Boolean()
    image=fields.Binary("Image")
    address=fields.Text()
    Age=fields.Integer()
    department_id=fields.Many2one(comodel_name='hms.department')
    department_capacity=fields.Integer(related='department_id.Num_of_Beds')
    status=fields.Selection([
        ("undetermined",'undetermined'),
        ("good","good"),
        ("fair","fair"),
        ("serious","serious")
    ],default="undetermined")
    doctors=fields.Many2many(comodel_name="hms.doctors")
    logs=fields.One2many(comodel_name="hms.logs",inverse_name="patient_id")
    email=fields.Char()

    def change_status(self):
        if self.status=="undetermined":
            self.status="good"
        elif self.status=="good":
            self.status="fair"
        elif self.status=="fair":
            self.status="serious"
        elif self.status=="serious":
            self.status="undetermined"
        self.logs.create({
           "patient_id": self.id,
           "description": self.fname + "'s status has changed to " + self.status,
        })

    @api.onchange('Age')
    def onchange_age(self):
        if self.Age<23:
            PCR_domain=[('checked','=',True)]
        else:
            PCR_domain=[]
        return {
                'domain':{'history':PCR_domain},
                'warning':{
                    'title':'age change',
                    'message':'PCR has been checked!'
                }
            }