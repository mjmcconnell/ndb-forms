"""Entry point for all requests to the app
"""
# third party imports
import webapp2


# Assign routes to the python classes above
ROUTES = [
    webapp2.Route('/', 'handlers.ExampleHandler'),
]
