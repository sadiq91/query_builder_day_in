from query_builder.app.handlers.filters.Filters import filterObject


def test_lists_match():
    list = filterObject.filters_list
    assert list == {
            'cash':'NumRange',
            'revenue': 'NumRange',
            'cid' : 'Multi',
            'cids' : 'Multi',
            'sector_context' : 'Multi',
            'sectors' : 'Multi',
            'trading_activity': 'Dates',
            'exclude_tps' : 'Bool',
            'ecommerce' : 'Bool',
            'aggregate' : 'Bool'

        }


