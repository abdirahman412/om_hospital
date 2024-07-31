from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "patient.tag"

    name = fields.Char(string='name', required='True')
    active = fields.Boolean(string="active", default=True, copy=False)
    color = fields.Integer(string="color")
    color2 = fields.Char(string="color2")
    sequence = fields.Integer(string="Sequence")

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)
        default['sequence'] = 10
        return super(PatientTag, self).copy(default=default)

    _sql_constraints = [
        ('unique_tag_name', 'unique (name, active)', 'name must be unique.'),
        ('check_sequence', 'check(sequence > 0)', 'Sequence must be non zero positive number.')
    ]