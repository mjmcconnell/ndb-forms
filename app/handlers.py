"""Template handlers, for injecting python into html templates.
"""
# third party imports
import jinja2
import webapp2

# local imports
import config
from serialiser import ExampleSerialiser


class SerialiseredHandler(webapp2.RequestHandler):

    template = None
    template_data = {}

    def _set_form(self):
        """Populates a form and adds it to the template data.
        """
        # Set serialiser
        serialiser = self.serialiser()
        r_id = self.request.route_kwargs.get('id')
        self.template_data['form'] = serialiser.form(self.request.POST, r_id)

    def _set_list(self):
        """Fetch all records and adds them to the template data.
        """
        serialiser = self.serialiser()
        self.template_data['records'] = serialiser.list(self.request.GET)


    def _get_jinja_template(self, template_file):
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(config.TEMPLATE_DIR),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True
        ).get_template(template_file)

    def render(self, template_file):
        """Handles setting the template values and rendering of the template.
        """
        # Grab template
        template = self._get_jinja_template(template_file)
        # Write response to the browser
        self.response.write(template.render(self.template_data))


class ExampleHandler(SerialiseredHandler):

    template = 'index.html'
    serialiser = ExampleSerialiser

    def get(self):
        """Default functionality for the get method
        """
        self._set_form()
        self.render(self.template)
