from fastapi.encoders import jsonable_encoder
from pydantic import parse_obj_as
from pydantic.main import BaseModel
import sqlalchemy as sa
from sqlalchemy.engine import Connection
from typing import Callable, Optional, TypeVar, Type, Union, Any
from uuid import UUID

from src.database.db_engine import metadata

T = TypeVar("T")


def parse_row(row, model: Type[T]) -> T:
    if "data" in row:
        return parse_obj_as(model, {**row.data, **row})
    else:
        return parse_obj_as(model, row)


def get_table_object(table_name: str):
    return metadata.tables[table_name]


def create_object(
    conn: Connection,
    object_name: str,
    object_data: Any,
    object_id: Optional[Any] = None,
    user_id: Optional[str] = None,
    parser: Optional[Callable[[Any], T]] = None,
) -> T:
    table = get_table_object(object_name)
    if isinstance(object_data, BaseModel):
        object_data = object_data.dict()

    values = {}
    for column in table.columns:
        if column.name != "data" and column.name in object_data:
            values[column.name] = object_data.pop(column.name)

    if "data" in table.columns:
        values["data"] = jsonable_encoder(object_data)

    if object_id is not None:
        values["id"] = object_id

    if user_id is not None:
        values["created_by"] = user_id

    stmt = sa.insert(table, values=values).returning(table)
    result = conn.execute(stmt).first()

    if parser is not None:
        return parser(result)
    else:
        return result


def update_object(
    conn: Connection,
    object_name: str,
    object_id: Union[str, UUID, int],
    object_data: Any,
    user_id: Optional[str] = None,
    parser: Optional[Callable[[Any], T]] = None,
    id_key: str = "id",
) -> T:
    table = get_table_object(object_name)
    if isinstance(object_data, BaseModel):
        object_data = object_data.dict()

    values = {}
    for column in table.columns:
        if column.name != "data" and column.name in object_data:
            values[column.name] = object_data.pop(column.name)

    if "data" in table.columns:
        values["data"] = jsonable_encoder(object_data)

    if user_id is not None:
        values["updated_by"] = user_id

    stmt = (
        table.update(values=values).where(
            table.c[id_key] == object_id).returning(table)
    )
    result = conn.execute(stmt).first()

    if parser is not None:
        return parser(result)
    else:
        return result


def delete_object(
    conn: Connection, object_name: str, object_id: Any, id_key: str = "id"
):
    table = get_table_object(object_name)
    conn.execute(table.delete(table.c[id_key] == object_id))


def delete_multi(conn: Connection, object_name: str, object_key: str, object_id: Any):
    table = get_table_object(object_name)
    conn.execute(table.delete(table.c[object_key] == object_id))


def clean_table(conn: Connection, object_name: str):
    table = get_table_object(object_name)
    conn.execute(table.delete())
