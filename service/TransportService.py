from repository.repository import (
    add_item_to_model,
    get_tansport_query_by_id,
    get_transport_query,
)


def get_transport(db, args, type):
    return get_transport_query(db, args, type)


def get_transport_by_id(db, id: int, type):
    return get_tansport_query_by_id(db, id, type)


def create_transport(db, item, type):
    return add_item_to_model(db, item, type)
