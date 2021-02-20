// Copyright (c) 2021, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('System', {
	onload: function (frm) {
		frm.fields_dict['lab_parameters'].grid.get_field("parameter").get_query = function (doc, cdt, cdn) {
			var parameter_t	= ["Lab Parameter","Both"]
			return {
				filters: {
					parameter_type: ['in', parameter_t],
				},
			};

		}
		frm.fields_dict['operational_parameters'].grid.get_field("parameter").get_query = function (doc, cdt, cdn) {
			var parameter_t	= ["Operational Parameter","Both"]
			return {
				filters: {
					parameter_type: ['in', parameter_t],
				},
			};

		}
	},
});
