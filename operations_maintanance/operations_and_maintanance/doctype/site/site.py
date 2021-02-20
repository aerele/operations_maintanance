# -*- coding: utf-8 -*-
# Copyright (c) 2021, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
import re
from frappe.model.document import Document

class Site(Document):
	def before_save(self):
		name = frappe.db.sql("""select name from `tabWarehouse` where warehouse_name = %s""",(self.name))
		parent_warehouse = frappe.db.sql("""select name from `tabWarehouse` where warehouse_name = %s""",("All Warehouses"))
		if(len(name) == 0):
			doc_e = frappe.get_doc({
            	'doctype': 'Warehouse',
            	'warehouse_name' : self.name,
            	'parent_warehouse': parent_warehouse[0][0]
        		})
			doc_e.save()
			self.warehouse = doc_e.name
		else:
			self.warehouse = name[0][0]

@frappe.whitelist()
def get_parameter(system_name):
	parameters = []
	new_system = json.loads(system_name)
	for system in new_system :
		temp = {}
		system_doc = frappe.get_doc("System",str(system))
		sub_parameter1 = []
		for lab_para in system_doc.lab_parameters:
			sub_parameter = []
			parameter_doc = frappe.get_doc("Parameter",str(lab_para.parameter))
			sub_parameter.append(lab_para.parameter)
			sub_parameter.append(lab_para.uom)
			sub_parameter.append(parameter_doc.data_type)
			sub_parameter.append(parameter_doc.parameter_type)
			sub_parameter1.append(sub_parameter)
		temp[system] = sub_parameter1
		parameters.append(temp)
	return parameters

@frappe.whitelist()
def get_consumable(system_name):
	consumable_list = []
	system_name = json.loads(system_name)
	for system in system_name:
		temp = {}
		system_doc = frappe.get_doc("System",str(system))
		sub_consum1 = []
		for consum in system_doc.consumables:
			sub_consum=[]
			sub_consum.append(consum.item)
			sub_consum.append(consum.uom)
			sub_consum1.append(sub_consum)
		temp[system] = sub_consum1
		consumable_list.append(temp)
	return consumable_list

@frappe.whitelist()
def get_operational_parameter(system_name):
	operational_list = []
	system_name = json.loads(system_name)
	for system in system_name:
		temp = {}
		system_doc = frappe.get_doc("System",str(system))
		sub_operation1 = []
		for operational in system_doc.operational_parameters:
			sub_operation=[]
			para_doc = frappe.get_doc("Parameter",str(operational.parameter))
			sub_operation.append(operational.parameter)
			sub_operation.append(operational.uom)
			sub_operation.append(operational.type)
			sub_operation.append(para_doc.data_type)
			sub_operation1.append(sub_operation)
		temp[system] = sub_operation1
		operational_list.append(temp)
	return operational_list