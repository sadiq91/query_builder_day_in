from query_builder.app.handlers.filters.filters_list_config.filters_list import filters



class Filter(object):
    filters_list = dict()

    def __init__(self):
        self.filters_list = filters.list
        self.param_key = None
        self.param_value = None


    def filter_query(self,query_para):
        for key,value in query_para.iteritems():
            if self.filters_list.get(key,None):

                classification = self.filters_list.get(key)

                instance = classification(key,value)



                instance.parse()


                self.param_value = instance.parsed_params[instance.query_param_key]
                self.param_key = instance.query_param_key




Filter = Filter()



