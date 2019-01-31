# -*- coding: utf-8 -*-
from schematics.types import StringType, ValidationError, MD5Type
from schematics.types.compound import ListType, ModelType
from zope.interface import implementer

from openregistry.assets.core.models import (
    AssetAdditionalClassification,
    IAsset, Asset as BaseAsset,
    Item,
    Debt
)


class IClaimRightsAsset(IAsset):
    """ Marker interface for claimRights assets """


@implementer(IClaimRightsAsset)
class Asset(BaseAsset):
    _internal_type = "claimRights"
    assetType = StringType(default="claimRights")
    items = ListType(ModelType(Item))
    debt = ModelType(Debt)
    additionalClassifications = ListType(ModelType(AssetAdditionalClassification), default=list())
    relatedLot = MD5Type(serialize_when_none=False)

    def validate_relatedLot(self, data, lot):
        if data['status'] == 'active' and not lot:
            raise ValidationError(u'This field is required.')
