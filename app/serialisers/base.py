# third-party imports
from google.appengine.ext import ndb

# local imports
from serialisers.widgets import get_widget


class ModelSerialiser(object):

    model = None

    def form(self, request_data, _id=None):
        """Builds a form for creating/updating ndb records.
        """
        return ModelForm(self.model, request_data, _id=)

    def list(self, request_data):
        """Returns a serialised list of objects from the ndb datastore
        """
        return []


class NDBModelForm(object):

    data = None
    fields = None

    def __init__(self, model, request_data, _id=):
        self.data = self._get_form_data(request_data, _id)
        self._populate(model, form_data)

    def __iter__(self):
        """Return each field in the form
        """
        for f in self.fields:
            yield f

    def _get_form_data(self, request_data, _id=None):
        """Returns a dictionary of key, values populating from any matching
        record, and request data
        """
        form_data = {}
        if _id:
            record = self.model.get_by_id(_id)
            if record:
                form_data = record.to_dict()

        form_data.update(request_data)
        return form_data

    def _populate(self, model, form_data)
        for _id, field in model._properties:
            form_value = form_data.get(_id)
            fields.append(FormField(_id, field, form_value))


class NDBFormField(object):

    def __init__(self, field_id, field, value=None):
        self.data = value
        self.id = field_id
        self.name = self._get_name(field)

        self._model_property = field

    def __call__(self):
        return self._get_widget(self)

    def _get_name(self, field):
        if field.verbose_name:
            return verbose_name
        return self._humanise(self.id)

    def _get_widget(field):
        return get_widget(self)

    def _humanise(value):
        """Converts underscore strings into human readable strings.
        """
        return value[0].upper() + value.replace('_', ' ')
