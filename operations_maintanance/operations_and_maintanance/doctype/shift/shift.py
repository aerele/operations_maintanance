# -*- coding: utf-8 -*-
# Copyright (c) 2021, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Shift(Document):
	def validate(self):
		for shift in self.shift_timings:
			shift_type_doc = frappe.new_doc("Shift Type")
			shift_type_doc.name  = self.project_number+"-"+shift.shift_name
			shift_type_doc.__newname = self.project_number+"-"+shift.shift_name
			shift_type_doc.project_number  = self.project_number
			if frappe.db.exists("Shift Type",{"name":self.project_number+"-"+shift.shift_name}):
				shift_type_doc = frappe.get_doc("Shift Type",self.project_number+"-"+shift.shift_name)
			shift_type_doc.start_time = shift.start_time
			shift_type_doc.end_time = shift.end_time
			shift_type_doc.save()

			
			

