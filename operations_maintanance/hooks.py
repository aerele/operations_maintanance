# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "operations_maintanance"
app_title = "Operations and Maintanance"
app_publisher = "Aerele Technologies Private Limited"
app_description = "Frappe application to manage workforce deployed for O&M at customer site levels"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@aerele.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/operations_maintanance/css/operations_maintanance.css"
# app_include_js = "/assets/operations_maintanance/js/operations_maintanance.js"

# include js, css files in header of web template
# web_include_css = "/assets/operations_maintanance/css/operations_maintanance.css"
# web_include_js = "/assets/operations_maintanance/js/operations_maintanance.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "operations_maintanance.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "operations_maintanance.install.before_install"
# after_install = "operations_maintanance.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "operations_maintanance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"operations_maintanance.tasks.all"
# 	],
# 	"daily": [
# 		"operations_maintanance.tasks.daily"
# 	],
# 	"hourly": [
# 		"operations_maintanance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"operations_maintanance.tasks.weekly"
# 	]
# 	"monthly": [
# 		"operations_maintanance.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "operations_maintanance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "operations_maintanance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "operations_maintanance.task.get_dashboard_data"
# }

