// Copyright (c) 2021, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Site Allocation', {
	project_number : function(frm){
		if (frm.doc.project_number != null){
			frappe.call({
				method: "frappe.client.get",
				args: {
					doctype: "Site Creation",
					name: frm.doc.project_number,
				},
				callback(r) {
					if(r.message) {
						frm.set_value("site_name",r.message["site_name"]);
					}
				}
			});
		}
	}
});
