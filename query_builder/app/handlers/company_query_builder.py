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

    def get_arguments(self, name):
        return self.query_params.get(name, [])

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

        # e.g. cash=1000-10000 or total_assets=-5000
        #self.parse_range_argument("cash")
        #self.parse_range_argument("revenue")

        #input to be filtered
        print "INPUT URL params"
        print self.query_params

        Filter.filter_query(self.query_params)
        self.parsed_params[Filter.param_key] = Filter.param_value





        # Args which may have multiple queries e.g. &cid=1&cid=2
        self.parse_get_arguments("cid", "cids")
        self.parse_get_arguments("sector_context", "sectors")

        # Special cases requiring custom logic
        #self.parse_trading_activity()

        self.parse_boolean_argument("exclude_tps", include_if_false=False)
        self.parse_boolean_argument("ecommerce", include_if_false=False)
        self.parse_boolean_argument("aggregate")

    def parse_trading_activity(self):
        """Parse trading activity parameters"""
        url_arg = self.get_argument('trading_activity', None)

        print "url_arg is  - - - " + url_arg

        if url_arg:
            self.parsed_params["trading_activity"] = dict()
            self.parse_dates(url_arg, "trading_activity")

    def parse_boolean_argument(self, arg, include_if_false=True):
        """Update parsed params with boolean arg value."""
        arg_val = self.parse_boolean(arg)
        if arg_val or include_if_false:
            self.parsed_params[arg] = arg_val


    def parse_get_arguments(self, arg, key=None):
        """Update parsed params if arg in request"""
        key = key or arg
        args = self.get_arguments(arg)
        if args:
            self.add_to_parsed_params(key, args)



    def parse_boolean(self, arg):
        """Parse boolean argument types
        
        Returns True or False if argument is present, otherwise None."""

        arg_param = self.get_argument(arg, None)
        if not arg_param:
            return None

        arg_check_int = re.search("^[0-1]$", arg_param)
        arg_check_bool = re.search("^true|false", arg_param.lower())
        if arg_check_int:
            return bool(int(arg_param))
        elif arg_check_bool:
            return {"true": True, "false": False}[arg_param.lower()]
        else:
            raise exceptions.ParameterValueError(key=arg, value=arg_param)



    def add_to_parsed_params(self, param_key, param_value):
        """Add params to parsed_params if arg exists"""
        self.parsed_params[param_key] = param_value

