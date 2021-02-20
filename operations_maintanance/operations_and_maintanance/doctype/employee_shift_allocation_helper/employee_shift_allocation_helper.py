# -*- coding: utf-8 -*-
# Copyright (c) 2021, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class EmployeeShiftAllocationHelper(Document):
	pass


@frappe.whitelist()
def get_data(project_number):
	shift_type = frappe.db.get_list("Shift Type", {'project_number': project_number}, ['name'])
	employee = []	
	data = frappe.db.get_list("Employee Site Allocation", {'name': project_number}, ['name'])
	print