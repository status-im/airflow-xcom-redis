# -*- coding: utf-8 -*-
from uuid import uuid4
from typing import Any
from airflow.models.xcom import BaseXCom
from airflow.providers.redis.hooks.redis import RedisHook

class XComRedisBackend(BaseXCom):
    PREFIX = 'xcom_redis://'
    # This connection needs to exist in advance
    CONN_ID = 'xcom_cache'

    @staticmethod
    def serialize_value(value: Any):
        hook = RedisHook(redis_conn_id=XComRedisBackend.CONN_ID)
        key = str(uuid4())
        # We use the default serializer, which pickles or JSONs
        hook.get_conn().set(key, BaseXCom.serialize_value(value))
        # Add prefix to make it clear where the value is stored.
        value = XComRedisBackend.PREFIX + key
        return BaseXCom.serialize_value(value)

    @staticmethod
    def deserialize_value(result) -> Any:
        result = BaseXCom.deserialize_value(result)
        prefix = XComRedisBackend.PREFIX
        if isinstance(result, str) and result.startswith(prefix):
            key = result.replace(prefix, "")
            hook = RedisHook(redis_conn_id=XComRedisBackend.CONN_ID)
            result = hook.get_conn().get(key)
            result = BaseXCom.deserialize_value(result)
        return result
