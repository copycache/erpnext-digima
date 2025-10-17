# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HappyMedItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.stock.doctype.item_default.item_default import ItemDefault
		from erpnext.stock.doctype.uom_conversion_detail.uom_conversion_detail import UOMConversionDetail
		from frappe.types import DF

		allow_negative_stock: DF.Check
		asset_category: DF.Link | None
		asset_naming_series: DF.Literal[None]
		auto_create_assets: DF.Check
		batch_number_series: DF.Data | None
		brand: DF.Link | None
		create_new_batch: DF.Check
		customer_code: DF.SmallText | None
		description: DF.TextEditor | None
		disabled: DF.Check
		has_batch_no: DF.Check
		has_expiry_date: DF.Check
		image: DF.AttachImage | None
		is_grouped_asset: DF.Check
		is_published: DF.Check
		item_code: DF.Data
		item_defaults: DF.Table[ItemDefault]
		item_group: DF.Link
		item_name: DF.Data | None
		naming_series: DF.Literal["STO-ITEM-.YYYY.-"]
		route: DF.Data | None
		standard_rate: DF.Currency
		stock_uom: DF.Link
		uoms: DF.Table[UOMConversionDetail]
		valuation_method: DF.Literal["", "FIFO", "Moving Average", "LIFO"]
		valuation_rate: DF.Currency
		warranty_period: DF.Data | None
		weight_per_unit: DF.Float
		weight_uom: DF.Link | None
	# end: auto-generated types
	pass
