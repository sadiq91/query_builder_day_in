from query_builder.app.handlers.filters.filters_classes.filter_bool import Bool
from query_builder.app.handlers.filters.filters_classes.filter_date import Date
from query_builder.app.handlers.filters.filters_classes.filter_multi import Multi
from query_builder.app.handlers.filters.filters_classes.filter_range import NumRange


class FiltersList(object):
    def __init__(self):
        self.list = {
            'cash':NumRange,
            'revenue': NumRange,
            'cid' : Multi,
            'sector_context' : Multi,
            'trading_activity': Date,
            'exclude_tps' : Bool,
            'ecommerce' : Bool,
            'aggregate' : Bool,

        }

filters = FiltersList()

