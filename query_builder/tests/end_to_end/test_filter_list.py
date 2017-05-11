from query_builder.app.handlers.filters.Filters import Filter
from query_builder.app.handlers.filters.filters_classes.filter_bool import Bool
from query_builder.app.handlers.filters.filters_classes.filter_date import Date
from query_builder.app.handlers.filters.filters_classes.filter_multi import Multi
from query_builder.app.handlers.filters.filters_classes.filter_range import NumRange
from query_builder.app.handlers.filters.Filters import Filter



def test_cash_filter():
    input = 'cash'
    expected = NumRange
    assert Filter.return_filter(input) == expected

def test_revenue_filter():
    input = 'revenue'
    expected = NumRange
    assert Filter.return_filter(input) == expected

def test_trading_activity_filter():
    input = 'trading_activity'
    expected = Date
    assert Filter.return_filter(input) == expected

def test_cid_filter():
    input = 'cid'
    expected = Multi
    assert Filter.return_filter(input) == expected

def test_sector_context_filter():
    input = 'sector_context'
    expected = Multi
    assert Filter.return_filter(input) == expected

def test_ecommerce_filter():
    input = 'ecommerce'
    expected = Bool
    assert Filter.return_filter(input) == expected

def test_sector_context_filter():
    input = 'sector_context'
    expected = Multi
    assert Filter.return_filter(input) == expected