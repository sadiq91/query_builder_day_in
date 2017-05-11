from query_builder.app.handlers.filters.Filters import Filter

filter_object = Filter()


keys_values = {'cash':['100-1000']}
print "dummy_file.py running"



#keys_values = {'cash':'100-1000','revenue':'1-1000', 'trading_activity' : '20150101-20160101', 'ecommerce' :'1'}

filter_object.filter_query(keys_values)