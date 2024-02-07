from typing import Any, ClassVar, Protocol, Dict

from dataclasses import dataclass, asdict, fields


class DataClass(Protocol):
    __dataclass_fields__: ClassVar[Dict]


@dataclass
class DTO:
    def as_dict(self, exclude_none: bool = False) -> dict:
        if exclude_none:
            return asdict(self, dict_factory=lambda field: {key: value for (key, value) in field if value is not None})
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Any:
        return cls(**data)  # type: ignore

    @classmethod
    def model_to_dto(cls, from_model_dt_class: DataClass):
        from_dt_dict = asdict(from_model_dt_class)

        field_names = [field.name for field in fields(cls)]
        filtered_fields = {}
        for key, value in from_dt_dict.items():
            if key in field_names:
                filtered_fields[key] = value

        return cls(**filtered_fields)
