// Copyright (c) 2021, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Site Allocation', {
});
frappe.ui.form.on("Employee Site Allocation Link",{
	employee:function(frm,cdt,cdn){
		var index = 0;
		var object = new Array();
		for (var id = frm.doc.links.length - 1; id >= 0; id--) {
			if (frm.doc.links[id].name == cdn) {
				index = id;
				break;
			}
		}
		frappe.call({
            
			method:"operations_maintanance.operations_and_maintanance.doctype.employee_site_allocation.employee_site_allocation.get_employee_role",
			args: {
				employee : frm.doc.links[index].employee
			},
			freeze: true,
			callback: (site) => {
                frm.fields_dict['employee_site_allocation_link'].grid.get_field("employee_role").get_query = function(doc) {
                    console.log("filter");
                    return {
                      filters:  {
                        "name" : ['in',site.message],
                      },
                    };
                }
			}
		})
	}
})
