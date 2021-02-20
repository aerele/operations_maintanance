// Copyright (c) 2021, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Shift Allocation Helper', {
	get_employee:function(frm){
		frappe.call({
			method:'operations_maintanance.operations_and_maintanance.doctype.employee_shift_allocation_helper.employee_shift_allocation_helper.get_data',
			args:{
				'project_number': frm.doc.project_number
			},
			callback:function(res){
				console.log(res);
			}
		})
	}
});
