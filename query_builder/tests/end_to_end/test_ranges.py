from query_builder.main import get_es_query
from query_builder.tests.end_to_end.es_query_template import full_es_query
from query_builder.exceptions import ParameterValueError

import pytest

def revenue_range_template(gte=None, lte=None):
    gte_lte = dict()
    if gte:
        gte_lte['gte'] = gte
    if lte:
        gte_lte['lte'] = lte

    return full_es_query({
        "nested": {
            "filter": {
                "bool": {
                    "must": [
                        {
                            "range": {
                                "financial_filters.revenue": gte_lte
                            }
                        }
                    ]
                }
            },
            "path": "financial_filters"
        }
    })


def test_range_both_ends():
    url = "/v1/company_query_builder?revenue=1-100"
    response = get_es_query(url)
    assert response == revenue_range_template(1, 100)

def test_range_bottom_end():
    url = "/v1/company_query_builder?revenue=1-"
    response = get_es_query(url)
    assert response == revenue_range_template(1, None)

def test_range_top_end():
    url = "/v1/company_query_builder?revenue=-100"
    response = get_es_query(url)
    assert response == revenue_range_template(None, 100)

#Test negative gte
def test_negative_gte():
    url = "/v1/company_query_builder?revenue=-1-100"
    response = get_es_query(url)
    assert response == revenue_range_template(-1,100)

#Test negative lte and gte
def test_negative_lte_gte():
    url = "/v1/company_query_builder?revenue=-100--1"
    response = get_es_query(url)
    assert response == revenue_range_template(-100,-1)


#Test lte < gte
def test_lte_lessThan_gte():
    url = "/v1/company_query_builder?revenue=-1--100"
    with pytest.raises(ParameterValueError):
        response = get_es_query(url)





