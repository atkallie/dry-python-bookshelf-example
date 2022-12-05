from mappers.entities import attrs
from mappers.entities import dataclasses
from mappers.entities import pydantic
from mappers.exceptions import MapperError


def _entity_factory(entity):
    if dataclasses._is_dataclass(entity):
        fields = dataclasses._get_fields(entity)
        factory = dataclasses._get_factory(fields, entity)
        return fields, factory
    elif pydantic._is_pydantic(entity):
        fields = pydantic._get_fields(entity)
        factory = pydantic._get_factory(fields, entity)
        return fields, factory
    elif attrs._is_attrs(entity):
        fields = attrs._get_fields(entity)
        factory = attrs._get_factory(fields, entity)
        return fields, factory
    else:
        raise MapperError
