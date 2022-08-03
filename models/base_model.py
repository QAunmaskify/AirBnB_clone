#!/usr/bin/python3
"""BaseModel Class"""


class BaseModel:
    """
    Super class BaseModel defines all common
    attributes: id, created_at, updated_at.

    id: assign unique string field when an instance
    is created.

    created_at: assign immutiable current datetime on
    instance creation.

    updated_at: assign mutiable current datetime on in-
    stance creation and later update.
    """
