from serialisers import base
from models.basic import BasicModel


class ExampleSerialiser(base.ModelSerialiser):

    model = BasicModel
