# third-party imports
from google.appengine.ext import ndb


def get_widget(field):
    """Returns an html widget for a given field based on its ndb property type
    """
    serialiser_field_mapping = {
        ndb.IntegerProperty: IntegerWidget(field),
        ndb.FloatProperty: IntegerWidget(field),
        ndb.BooleanProperty: SwitchWidget(field),
        ndb.StringProperty: TextWidget(field),
        ndb.TextProperty: TextareaWidget(field),
        ndb.DateTimeProperty: DatetimeWidget(field),
        ndb.DateProperty: DateWidget(field),
        ndb.TimeProperty: TimeWidget(field),
        ndb.GeoPtProperty: GeoptWidget(field),
        ndb.KeyProperty: SelectWidget(field),
        ndb.UserProperty: SelectWidget(field),
        ndb.StructuredProperty: SelectWidget(field),
        ndb.StructuredProperty: MultiSelectWidget(field),
        ndb.JsonProperty: TextareaWidget(field),
        ndb.PickleProperty: TextareaWidget(field),
        ndb.ComputedProperty: TextWidget(field, read_only=True),
    }

    m_prop = field._model_property
    return serialiser_field_mapping.get(m_prop, TextWidget(self))


class BaseWidget(object):

    def __init__(self, field, **kargs):
        pass

    def __call__(self):
        return ''


class IntegerWidget(BaseWidget):
    pass

class SwitchWidget(BaseWidget):
    pass

class TextWidget(BaseWidget):
    pass

class TextareaWidget(BaseWidget):
    pass

class DatetimeWidget(BaseWidget):
    pass

class DateWidget(BaseWidget):
    pass

class TimeWidget(BaseWidget):
    pass

class GeoptWidget(BaseWidget):
    pass

class SelectWidget(BaseWidget):
    pass

class MultiSelectWidget(BaseWidget):
    pass

