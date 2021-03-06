from app.db import db
from app import json


class Key(db.Model, json.Serialisable):

    __tablename__ = 'key'

    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.String())
    private_key = db.Column(db.String())

    def json_format(self):
        jsondata = {}

        def append(name, parameter):
            value = parameter(self)
            if value is not None:
                jsondata[name] = value

        append('id', lambda obj: obj.id)
        append('private_key', lambda obj: obj.private_key)
        append('public_key', lambda obj: obj.public_key)

        return jsondata

    def object_hook(dct):
        _id = dct.get('id')
        _private_key = dct.get('private_key')
        _public_key = dct.get('public_key')

        key = Key()
        key.id = _id
        key.private_key = _private_key
        key.public_key = _public_key

        return key
