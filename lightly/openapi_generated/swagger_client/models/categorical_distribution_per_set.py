# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
try:
    # Pydantic >=v1.10.17
    from pydantic.v1 import BaseModel, Field
except ImportError:
    # Pydantic v1
    from pydantic import BaseModel, Field
from lightly.openapi_generated.swagger_client.models.categorical_distribution import CategoricalDistribution

class CategoricalDistributionPerSet(BaseModel):
    """
    CategoricalDistributionPerSet
    """
    input: CategoricalDistribution = Field(...)
    selected: CategoricalDistribution = Field(...)
    random: CategoricalDistribution = Field(...)
    preselected_datapool: Optional[CategoricalDistribution] = Field(None, alias="preselectedDatapool")
    selected_with_datapool: Optional[CategoricalDistribution] = Field(None, alias="selectedWithDatapool")
    __properties = ["input", "selected", "random", "preselectedDatapool", "selectedWithDatapool"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = "forbid"

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> CategoricalDistributionPerSet:
        """Create an instance of CategoricalDistributionPerSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of input
        if self.input:
            _dict['input' if by_alias else 'input'] = self.input.to_dict(by_alias=by_alias)
        # override the default output from pydantic by calling `to_dict()` of selected
        if self.selected:
            _dict['selected' if by_alias else 'selected'] = self.selected.to_dict(by_alias=by_alias)
        # override the default output from pydantic by calling `to_dict()` of random
        if self.random:
            _dict['random' if by_alias else 'random'] = self.random.to_dict(by_alias=by_alias)
        # override the default output from pydantic by calling `to_dict()` of preselected_datapool
        if self.preselected_datapool:
            _dict['preselectedDatapool' if by_alias else 'preselected_datapool'] = self.preselected_datapool.to_dict(by_alias=by_alias)
        # override the default output from pydantic by calling `to_dict()` of selected_with_datapool
        if self.selected_with_datapool:
            _dict['selectedWithDatapool' if by_alias else 'selected_with_datapool'] = self.selected_with_datapool.to_dict(by_alias=by_alias)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CategoricalDistributionPerSet:
        """Create an instance of CategoricalDistributionPerSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CategoricalDistributionPerSet.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in CategoricalDistributionPerSet) in the input: " + str(obj))

        _obj = CategoricalDistributionPerSet.parse_obj({
            "input": CategoricalDistribution.from_dict(obj.get("input")) if obj.get("input") is not None else None,
            "selected": CategoricalDistribution.from_dict(obj.get("selected")) if obj.get("selected") is not None else None,
            "random": CategoricalDistribution.from_dict(obj.get("random")) if obj.get("random") is not None else None,
            "preselected_datapool": CategoricalDistribution.from_dict(obj.get("preselectedDatapool")) if obj.get("preselectedDatapool") is not None else None,
            "selected_with_datapool": CategoricalDistribution.from_dict(obj.get("selectedWithDatapool")) if obj.get("selectedWithDatapool") is not None else None
        })
        return _obj
