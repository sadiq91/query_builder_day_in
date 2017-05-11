from query_builder.app.handlers.filters_list import filters



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

                self.param_value = instance.parsed_params[key]
                self.param_key = key

                print "Filter self.param_value is"
                print self.param_value
                print "Filter self.param_key is"
                print self.param_key




Filter = Filter()



