from query_builder.app.handlers.filters.filters_classes.Bool import Bool
from query_builder.app.handlers.filters.filters_classes.Date import Date
from query_builder.app.handlers.filters.filters_classes.Multi import Multi
from query_builder.app.handlers.filters.filters_classes.Range import NumRange


class FiltersList(object):
    def __init__(self):
        self.list = {
            'cash':NumRange,
            'revenue': NumRange,
            'cid' : Multi,
            'cids' : Multi,
            'sector_context' : Multi,
            'sectors' : Multi,
            'trading_activity': Date,
            'exclude_tps' : Bool,
            'ecommerce' : Bool,
            'aggregate' : Bool,

        }

filters = FiltersList()

