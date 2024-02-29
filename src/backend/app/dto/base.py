from typing import Any, ClassVar, Protocol, Dict, Sequence

from dataclasses import dataclass, asdict, fields


class DataClass(Protocol):
    __dataclass_fields__: ClassVar[Dict]


@dataclass
class DTO:
    def as_dict(self, exclude: Sequence | None = None, exclude_none: bool = False) -> dict:
        def exclude_none_factory(field):
            return {key: value for (key, value) in field if value is not None}

        def exclude_factory(field):
            return {key: value for (key, value) in field if key not in exclude}  # type: ignore

        if exclude_none:
            return asdict(self, dict_factory=exclude_none_factory)
        if exclude:
            return asdict(self, dict_factory=exclude_factory)

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


@dataclass
class PaginationBaseDTO(DTO):
    page: int = 1
    limit: int | None = None
    all: int | None = None
    offset: int | None = 0

    def __post_init__(self):
        self.offset = self.limit * (self.page - 1) if self.limit else self.page
