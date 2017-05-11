from query_builder.app.handlers.filters.Filters import Filter
from query_builder.app.handlers.filters.filters_classes.Bool import Bool
from query_builder.app.handlers.filters.filters_classes.Date import Date
from query_builder.app.handlers.filters.filters_classes.Multi import Multi
from query_builder.app.handlers.filters.filters_classes.Range import NumRange


def test_lists_match():
    filters = Filter.filters_list

    expected = {
        'cash': NumRange,
        'revenue': NumRange,
        'cid': Multi,
        'cids': Multi,
        'sector_context': Multi,
        'sectors': Multi,
        'trading_activity': Date,
        'exclude_tps': Bool,
        'ecommerce': Bool,
        'aggregate': Bool,

    }

    for key, value in filters.items():
        assert value == expected.get(key)





