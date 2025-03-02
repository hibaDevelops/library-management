import abc

from flask import request
from flask_restful import reqparse


class RequestInterface(metaclass=abc.ABCMeta):
    def __init_subclass__(cls, **kwargs):
        cls.childKeys = {}
        cls.parser = None
        cls.result = None
        cls.req = kwargs.get("req", None)

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "get_request_parser")
            and callable(subclass.get_request_parser)
            and hasattr(subclass, "init_parser")
            and callable(subclass.init_parser)
            and hasattr(subclass, "get_data")
            and callable(subclass.get_data)
        )

    @classmethod
    def get_request_parser(cls):
        if not cls.parser:
            cls.parser = reqparse.RequestParser(bundle_errors=True)
            cls.init_parser(cls)

        return cls.parser

    @classmethod
    def get_data(cls, req=None):
        req = req if req else cls.req
        parser = cls.get_request_parser()
        cls.result = parser.parse_args(req=req)

        request_json = request.get_json(silent=True)
        original_request = request_json if request_json else request.values

        for arg in cls.parser.args:
            if (
                arg.name in original_request
                and (arg.dest or arg.name) not in cls.result
            ):
                cls.result[(arg.dest or arg.name)] = original_request[arg.name]

            for key, value in cls.childKeys.items():
                cls.result[key] = value

            return cls.result


class DummyRequest(dict):
    def __init__(self, data: dict):
        super().__init__()
        self.json = data
        self.unparsed_arguments = {}
