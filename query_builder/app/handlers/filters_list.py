from query_builder.app.handlers.filters.NumRange import NumRange
from query_builder.app.handlers.filters.Date import Date
from query_builder.app.handlers.filters.Bool import Bool
from query_builder.app.handlers.filters.Multi import Multi


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

