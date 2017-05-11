import re
from query_builder import exceptions



class Bool():
    parsed_params = dict()

    def __init__(self, query_param_key, query_param_value):
        self.query_param_key = query_param_key
        self.query_param_value = query_param_value

    def parse(self):

        self.parse_boolean_argument(self.query_param_key, include_if_false=False)

    def parse_boolean_argument(self, arg, include_if_false=True):
        """Update parsed params with boolean arg value."""
        arg_val = self.parse_boolean(arg)

        if arg_val or include_if_false:
            self.parsed_params[arg] = arg_val



    def parse_boolean(self, arg):
        """Parse boolean argument types

        Returns True or False if argument is present, otherwise None."""

        arg_param = self.query_param_value[0]
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

