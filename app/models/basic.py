"""Core datastore models and base modals.
"""

# third-party imports
from google.appengine.ext import ndb


class ChildModel(ndb.Model):
    """Class used to respresent child model properties

    KeyProperty
    StructuredProperty
    """

    string_field = ndb.StringProperty()


class BasicModel(ndb.Model):
    """Common data/operations for all storage models
    """

    int_field = ndb.IntegerProperty()
    float_field = ndb.FloatProperty()
    boolean_field = ndb.BooleanProperty()
    string_field = ndb.StringProperty()
    text_field = ndb.TextProperty()
    blob_field = ndb.BlobProperty()
    datetime_field = ndb.DateTimeProperty()
    date_field = ndb.DateProperty()
    time_field = ndb.TimeProperty()
    geopt_field = ndb.GeoPtProperty()
    key_field = ndb.KeyProperty()
    blobkey_field = ndb.BlobKeyProperty()
    user_field = ndb.UserProperty()
    single_structured_field = ndb.StructuredProperty(ChildModel)
    repeated_structured_field = ndb.StructuredProperty(ChildModel, repeated=True)
    json_field = ndb.JsonProperty()
    pickle_field = ndb.PickleProperty()
    computed_field = ndb.ComputedProperty(lambda self: self.string_field.upper())
