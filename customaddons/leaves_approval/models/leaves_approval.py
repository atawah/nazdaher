from odoo import models, fields, api, exceptions

class LeavesApproval(models.Model):
    _inherit = 'hr.leave'

    @api.depends('field_name')
    def _get_next_approver(self):
        # Logic to get the next person in the organization chart
        # You can customize this method based on your organization's structure
        # For example, you can use the 'parent_id' field to traverse the organization chart

        # Define the next_approver_id variable
        next_approver_id = None
        # Return the next approver's user ID
        return next_approver_id

    def _check_approver_on_leave(self):
        for leave in self:
            if leave.state == 'confirmed' and leave.employee_id.parent_id and hasattr(leave.employee_id.parent_id, 'on_leave') and leave.employee_id.parent_id.on_leave == True:
                next_approver_id = leave._get_next_approver()
                if next_approver_id:
                    leave.write({'holiday_status_id': next_approver_id})

    def _check_leave_access(self):
        for leave in self:
            user = self.env.user
            if user.has_group('base.group_user') and not user.has_group('base.group_hr_user'):
                if leave.employee_id.parent_id and leave.employee_id.parent_id.user_id != user and leave.employee_id != user.employee_id:
                    raise exceptions.UserError("You are not authorized to view this leave request.")
                elif leave.employee_id == user.employee_id:
                    raise exceptions.UserError("You cannot approve your own leave request.")
            elif user.has_group('base.group_hr_user'):
                if leave.employee_id.parent_id and leave.employee_id.parent_id.on_leave == True:
                    next_approver_id = leave._get_next_approver()
                    if next_approver_id:
                        leave.write({'holiday_status_id': next_approver_id})
                else:
                    raise exceptions.UserError("You are not authorized to view this leave request.")

    def action_approve(self):
        self._check_leave_access()
        self._check_approver_on_leave()
        return super(LeavesApproval, self).action_approve()
        

    

