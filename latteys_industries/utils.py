import frappe
from frappe import _
from erpnext.accounts.utils import get_fiscal_year


@frappe.whitelist()
def get_fisc_year(date):
    if date:
        fiscal_year = get_fiscal_year(date)[0]
    else:
        fiscal_year = frappe.defaults.get_user_default(
            "fiscal_year")
    fisc_year = fiscal_year[2:5] + fiscal_year[-2:]
    return fisc_year