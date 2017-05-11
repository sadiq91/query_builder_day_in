import datetime
import re
import urlparse

from query_builder import exceptions
from query_builder.app.elastic.piston import Piston
from query_builder.app.handlers.pagination import Pagination
from query_builder.config.app import settings
from query_builder.app.handlers.filters.Filters import Filter


class CompanyQueryBuilder(object):
    """Company Query Builder main handler."""

    def __init__(self, url):
        parsed_url = urlparse.urlparse(url)
        self.query_params = urlparse.parse_qs(parsed_url.query)
        self.valid_args = settings.COMPANIES_FILTERS
        self.piston = Piston()
        self.parsed_params = dict()

    def get(self):
        """Handle get requests to /company_query_builder"""
        self.pagination = Pagination(limit=self.get_argument("limit", None),
                                     offset=self.get_argument("offset", 0))
        self.validate_args(self.valid_args)
        self.parse_parameters()
        self.parsed_params["size"] = self.pagination.page_size
        self.parsed_params["from"] = self.pagination.page_offset
        es_query = self.piston.company_search(self.parsed_params)

        return es_query

    def get_argument(self, name, default=None):
        return self.query_params.get(name, [default])[-1]


    def validate_args(self, valid_arguments=None, required_args=None):
        """Check argument parameters are valid and present raise exception if not"""
        request_set = set(self.query_params.keys())
        if valid_arguments:

            invalid = request_set - set(valid_arguments)
            if invalid:
                raise exceptions.ParameterKeyError(key=", ".join(invalid))

        if required_args:
            missing = set(required_args) - request_set
            if missing:
                raise exceptions.ParameterKeyError(key=", ".join(missing))


    def parse_parameters(self, org=None, model_config=None):
        """Parse the URL parameters and build parsed_params dict."""


        Filter.filter_query(self.query_params)

        #self.parsed_params.update(Filter.parsed_params)

        self.parsed_params[Filter.param_key] = Filter.param_value



        #Passing a dict as opposed to a key+value separately seem to break the assertion in the test-files...
        #self.parsed_params.update(Filter.parsed_params)






