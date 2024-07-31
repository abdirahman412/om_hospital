from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'

    name = fields.Char(string='sequence', default='new')
    patient_id = fields.Many2one('hospital.patient', string="patient",ondelete='cascade')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time',default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date',default=fields.Date.context_today)
    ref = fields.Char(string='Reference', help="Reference from patient record")
    prescription = fields.Html(string='prescription')
    priority = fields.Selection([
        ('0', 'normal'),
        ('1', 'low'),
        ('2', 'high'),
        ('3', 'very high')], string="priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string='status', required='True', tracking=True)
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_price= fields.Boolean(string="Hide Sales Price")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals)

    def unlink(self):
        print("Test...............................")
        if self.state == 'done':
            raise ValidationError(_("you cannot delete appointment with done status !"))
        return super(HospitalAppointment, self).unlink()

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button Clicked !!!!!!!!!!!!")
        return {
               'effect':{
               'massage': 'Click Successful',
               'type':'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'in consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
       action = self.env.ref('om_hospital.action_cancel_appointment')
       return action
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

class AppointmentPharmacy(models.Model):
     _name = "appointment.pharmacy.lines"
     _description = "appointment pharmacy lines"

     product_id = fields.Many2one('product.product', required=True)
     price_unit = fields.Float(related='product_id.list_price')
     qty = fields.Integer(string='quantity',default=1)
     appointment_id = fields.Many2one('hospital.appointment', string='Appointment')