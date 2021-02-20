# -*- coding: utf-8 -*-
# Copyright (c) 2021, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EmployeeSiteAllocation(Document):
	pass

@frappe.whitelist()
def get_employee_role(employee):
	role = []
	print("triggered")
	return(role)
# select role from `tabUser` as us inner join `tabHas Role` as hr on hr.parent = us.name where us.name ="example@gmail.com"\G;
