from query_builder.app.handlers.filters_list import filters



class Filter(object):
    filters_list = dict()
    es_query = dict()

    def __init__(self):
        self.filters_list = filters.list


    def filter_query(self,query_para):
        for key,value in query_para.iteritems():
            if self.filters_list.get(key,None):

                classification = self.filters_list.get(key)

                query_param_key = key
                query_param_value = value

                instance = classification(query_param_key, query_param_value)



                instance.parse()




        es_query = instance.parsed_params

        return es_query





filterObject = Filter()



