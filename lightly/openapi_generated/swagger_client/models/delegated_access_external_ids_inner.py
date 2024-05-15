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
from pydantic import Extra,  BaseModel, Field, StrictStr, constr, validator

class DelegatedAccessExternalIdsInner(BaseModel):
    """
    DelegatedAccessExternalIdsInner
    """
    external_id: constr(strict=True, min_length=10) = Field(..., alias="externalId", description="The external ID specified when creating the role. More information can be found here: - https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html - https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_externalid ")
    user_id: Optional[StrictStr] = Field(None, alias="userId")
    team_id: Optional[StrictStr] = Field(None, alias="teamId")
    __properties = ["externalId", "userId", "teamId"]

    @validator('external_id')
    def external_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9_+=,.@:\/-]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_+=,.@:\/-]+$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = Extra.forbid

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> DelegatedAccessExternalIdsInner:
        """Create an instance of DelegatedAccessExternalIdsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DelegatedAccessExternalIdsInner:
        """Create an instance of DelegatedAccessExternalIdsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DelegatedAccessExternalIdsInner.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in DelegatedAccessExternalIdsInner) in the input: " + str(obj))

        _obj = DelegatedAccessExternalIdsInner.parse_obj({
            "external_id": obj.get("externalId"),
            "user_id": obj.get("userId"),
            "team_id": obj.get("teamId")
        })
        return _obj
