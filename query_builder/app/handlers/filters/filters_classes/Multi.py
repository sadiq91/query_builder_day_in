


from query_builder.app.handlers.filters.filters_list_config.multi_class_filters import multi_filters




class Multi():

    parsed_params = dict()



    def __init__(self, query_param_key, query_param_value):
        self.query_param_key = multi_filters.multi_class_filters_list[query_param_key]
        self.query_param_value = query_param_value
        self.query_params = {self.query_param_key: self.query_param_value}



    def parse(self):
        self.parse_get_arguments(self.query_param_key)



    def parse_get_arguments(self, arg, key=None):
        """Update parsed params if arg in request"""
        key = key or arg
        args = self.query_param_value
        if args:
            self.parsed_params[key] = args


