
from query_builder import exceptions
import re
import urlparse





class NumRange():

   parsed_params =dict()


   def __init__(self,query_param_key, query_param_value):
       self.query_param_key = query_param_key
       self.query_param_value = query_param_value
       self.query_params = {self.query_param_key : self.query_param_value}

   def parse(self):

        #arg == string (key)

       """Update parsed params if arg in request"""
       self.lower, self.upper = self.parse_range(self.query_param_value)


       if self.lower or self.upper:
           self.add_to_parsed_params(self.query_param_key, {"gte": self.lower, "lte": self.upper})

   def parse_range(self):
        """Parser for arguments that are numerical range types.

        Takes the argument to check as an input (e.g. revenue).
        Expect an argument of the format: n-N
        Returns lower and upper bounds. Negative values are permitted.
        Returns None if parsing failed."""

        arg_param = self.query_param_value
        if arg_param:
            exp = "^([-]*[0-9]*)[-]([-]*[0-9]*)$"
            m = re.search(exp, arg_param)
            if not m:
                raise exceptions.ParameterValueError(key=arg, value=arg_param)

            lbound, ubound = None, None
            # Parse lower bound
            if m.group(1):
                try:
                    lbound = int(m.group(1))
                except ValueError:
                    raise exceptions.ParameterValueError(key=arg, value=arg_param)

            # Parse upper bound
            if m.group(2):
                try:
                    ubound = int(m.group(2))
                except ValueError:
                    raise exceptions.ParameterValueError(key=arg, value=arg_param)

            if lbound != None and ubound != None and lbound > ubound:
                raise exceptions.ParameterValueError(key=arg, value=arg_param)

            return lbound, ubound
        else:
            return None, None

   def get_argument(self, name, default=None):
        return self.query_params.get(name, [default])[-1]

   def add_to_parsed_params(self, param_key, param_value):
       """Add params to parsed_params if arg exists"""
       self.parsed_params[param_key] = param_value
