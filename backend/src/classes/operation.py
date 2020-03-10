from enum import Enum


class Operation(Enum):
    FIND = 'find'
    INSERT = 'insert'
    ONE = '_one'
    MANY = '_many'
    ONE_AND_DELETE = '_one_and_delete'
    ONE_AND_REPLACE = '_one_and_replace'
    ONE_AND_UPDATE = '_one_and_update'
    COUNT = 'count'
    DISTINCT = 'distinct'
    AND_MODIFY = '_and_modify'
    UPDATE = 'update'
