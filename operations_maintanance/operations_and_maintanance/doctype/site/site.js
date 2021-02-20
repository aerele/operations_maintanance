// Copyright (c) 2021, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Site', {
	onload: function (frm) {
		frm.fields_dict['systems'].grid.get_field("system_name").get_query = function (doc) {
			var process = [];
			for (let i in frm.doc.process_name) {
				process.push(frm.doc.process_name[i].process_name);
			}
			return {
				filters: {
					"process_name": ['in', process],
				},
			};
		},
			frm.fields_dict['lab_parameters'].grid.get_field("parameter").get_query = function (doc, cdt, cdn) {
				var parameter_t = ["Lab Parameter", "Both"]
				return {
					filters: {
						parameter_type: ['in', parameter_t],
					},
				};

			}
		frm.fields_dict['operational_parameters'].grid.get_field("parameter").get_query = function (doc, cdt, cdn) {
			var parameter_t = ["Operational Parameter", "Both"]
			return {
				filters: {
					parameter_type: ['in', parameter_t],
				},
			};

		}

	},
	get_parameter: function (frm) {
		var system = [];
		for (let i in frm.doc.systems) {
			system.push(frm.doc.systems[i].system_name);
		}
		var object = new Array();
		var u = 0;
		var v = 0;
		var w = 0;
		frappe.call({
			method: "operations_maintanance.operations_and_maintanance.doctype.site.site.get_parameter",
			args: {
				system_name: system,
			},
			freeze: true,
			callback: (r) => {
				frm.clear_table("lab_parameters");
				if (r.message) {
					for (let i in r.message) {
						let temp_system = system[i];
						for (let j in r.message[i][temp_system]) {
							object[u] = frm.add_child("lab_parameters");
							object[u].system = temp_system;
							object[u].parameter = r.message[i][temp_system][j][0];
							object[u].uom = r.message[i][temp_system][j][1];
							object[u].data_type = r.message[i][temp_system][j][2];
						}
						u = u + 1;
						frm.refresh_field("lab_parameters");
					}
				}
			},
		});
		frappe.call({
			method: "operations_maintanance.operations_and_maintanance.doctype.site.site.get_consumable",
			args: {
				system_name: system,
			},
			freeze: true,
			callback: (r) => {
				frm.clear_table("consumables");
				if (r.message) {
					for (let i in r.message) {
						let temp_system = system[i];
						for (let j in r.message[i][temp_system]) {
							object[v] = frm.add_child("consumables");
							object[v].system = temp_system;
							object[v].item = r.message[i][temp_system][j][0];
							object[v].uom = r.message[i][temp_system][j][1];
						}
						v = v + 1;
						frm.refresh_field("consumables");
					}
				}
			},
		});
		frappe.call({
			method: "operations_maintanance.operations_and_maintanance.doctype.site.site.get_operational_parameter",
			args: {
				system_name: system,
			},
			freeze: true,
			callback: (r) => {
				frm.clear_table("operational_parameters");
				if (r.message) {
					for (let i in r.message) {
						let temp_system = system[i];
						for (let j in r.message[i][temp_system]) {
							object[w] = frm.add_child("operational_parameters");
							object[w].system = temp_system;
							object[w].parameter = r.message[i][temp_system][j][0];
							object[w].uom = r.message[i][temp_system][j][1];
							object[w].type = r.message[i][temp_system][j][2];
							object[w].data_type = r.message[i][temp_system][j][3];
						}
						w = w + 1;
						frm.refresh_field("operational_parameters");
					}
				}
			},
		});
	},
});
