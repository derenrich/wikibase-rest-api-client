"""Contains all the data models used in inputs/outputs"""

from .aliases import Aliases
from .aliases_add_request import AliasesAddRequest
from .aliases_patch_request import AliasesPatchRequest
from .description_replace_request import DescriptionReplaceRequest
from .descriptions import Descriptions
from .descriptions_patch_request import DescriptionsPatchRequest
from .error import Error
from .get_item_fields_item import GetItemFieldsItem
from .get_property_fields_item import GetPropertyFieldsItem
from .item import Item
from .item_aliases import ItemAliases
from .item_descriptions import ItemDescriptions
from .item_labels import ItemLabels
from .item_sitelinks import ItemSitelinks
from .item_statements import ItemStatements
from .label_replace_request import LabelReplaceRequest
from .labels import Labels
from .labels_patch_request import LabelsPatchRequest
from .mediawiki_edit import MediawikiEdit
from .patch_document import PatchDocument
from .patch_document_patch_item import PatchDocumentPatchItem
from .patch_document_patch_item_op import PatchDocumentPatchItemOp
from .property_ import Property
from .property_aliases import PropertyAliases
from .property_descriptions import PropertyDescriptions
from .property_info import PropertyInfo
from .property_labels import PropertyLabels
from .property_statements import PropertyStatements
from .qualifier import Qualifier
from .reference import Reference
from .sitelink import Sitelink
from .sitelink_patch_request import SitelinkPatchRequest
from .sitelink_replace_request import SitelinkReplaceRequest
from .statement import Statement
from .statement_patch_request import StatementPatchRequest
from .statement_rank import StatementRank
from .statement_request import StatementRequest
from .value import Value
from .value_type import ValueType

__all__ = (
    "Aliases",
    "AliasesAddRequest",
    "AliasesPatchRequest",
    "DescriptionReplaceRequest",
    "Descriptions",
    "DescriptionsPatchRequest",
    "Error",
    "GetItemFieldsItem",
    "GetPropertyFieldsItem",
    "Item",
    "ItemAliases",
    "ItemDescriptions",
    "ItemLabels",
    "ItemSitelinks",
    "ItemStatements",
    "Labels",
    "LabelsPatchRequest",
    "LabelReplaceRequest",
    "MediawikiEdit",
    "PatchDocument",
    "PatchDocumentPatchItem",
    "PatchDocumentPatchItemOp",
    "Property",
    "PropertyAliases",
    "PropertyDescriptions",
    "PropertyLabels",
    "PropertyStatements",
    "Qualifier",
    "PropertyInfo",
    "Value",
    "ValueType",
    "Reference",
    "Sitelink",
    "SitelinkPatchRequest",
    "SitelinkReplaceRequest",
    "Statement",
    "StatementPatchRequest",
    "StatementRank",
    "StatementRequest",
)
