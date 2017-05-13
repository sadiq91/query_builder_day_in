from query_builder.app.handlers.filters.filters_list_config.filters_list import filters



class Filter(object):
    filters_list = dict()
    parsed_params = dict()
    def __init__(self):
        self.filters_list = filters.list
        self.param_key = None
        self.param_value = None


    def return_filter(self, query_input):
        if self.filters_list.get(query_input,None):
            return self.filters_list.get(query_input)
        else:
            return False

    def filter_query(self,query_para):
        for key,value in query_para.iteritems():
            if self.filters_list.get(key,None):

                classification = self.filters_list.get(key)

                instance = classification(key,value)



                instance.parse()

                #self.parsed_params = instance.parsed_params



              
                if instance.parsed_params.get(instance.query_param_key,None):

                    self.param_value = instance.parsed_params[instance.query_param_key]
                    self.param_key = instance.query_param_key
                else:

                    self.parsed_params[instance.query_param_key] = instance.parsed_params
                


Filter = Filter()



