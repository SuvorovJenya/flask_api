from repository.TransportRepository import (
    create_transport,
    get_transport_by_id,
    get_transport,
)


def get_transport(db, args, type):
    return get_transport(db, args, type)


def get_transport_by_id(db, id: int, type):
    return get_transport_by_id(db, id, type)


def create_transport(db, item, type):
    return create_transport(db, item, type)
