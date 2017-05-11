import datetime



from query_builder import exceptions



class Date():

    parsed_params = dict()

    def __init__(self, query_param_key, query_param_value):
        self.query_param_key = query_param_key
        self.query_param_value = query_param_value
        self.query_params = {self.query_param_key: self.query_param_value}

    def parse(self):
        self.parse_dates(self.query_param_value[0], self.query_param_key)


    def parse_date(self, arg):
        """ Parse a date argument """

        if arg:
            try:

                parameter = datetime.datetime.strptime(
                    arg, '%Y%m%d').date().isoformat()
                return parameter
            except Exception as e:
                raise exceptions.ParameterValueError(key=arg, value=arg,
                                                     message=e.message)

    def parse_dates(self, url_arg, key):
        """Parse the dates arguments from URL params."""
        datefrom, dateto = url_arg.split('-')
        datefrom = self.parse_date(datefrom)
        dateto = self.parse_date(dateto)
        if datefrom or dateto:
            self.parsed_params[key] = {}
            if datefrom:
                self.parsed_params[key]["gte"] = datefrom
            if dateto:
                self.parsed_params[key]["lte"] = dateto