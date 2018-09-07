# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    has_group_show_line_subtotals_tax_excluded = fields.Boolean(
        "Show line subtotals without taxes (B2B)",
        compute='_compute_groups_id', inverse='_inverse_groups_id',
        group_xml_id='account.group_show_line_subtotals_tax_excluded')

    has_group_show_line_subtotals_tax_included = fields.Boolean(
        "Show line subtotals with taxes included (B2C)",
        compute='_compute_groups_id', inverse='_inverse_groups_id',
        group_xml_id='account.group_show_line_subtotals_tax_included')

    has_group_warning_account = fields.Boolean(
        'A warning can be set on a partner (Account)', compute='_compute_groups_id', inverse='_inverse_groups_id',
        group_xml_id='account.group_warning_account')

    has_group_cash_rounding = fields.Boolean(
        'Allow the cash rounding management', compute='_compute_groups_id', inverse='_inverse_groups_id',
        group_xml_id='account.group_cash_rounding')

    group_account_user = fields.Selection(
        selection=lambda self: self._get_group_selection('base.module_category_accounting_and_finance'),
        string='Accounting', compute='_compute_groups_id', inverse='_inverse_groups_id',
        category_xml_id='base.module_category_accounting_and_finance')
