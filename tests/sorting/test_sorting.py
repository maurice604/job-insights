import pytest
from src.sorting import sort_by

jobs = [
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-20"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-10"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-01-01"},
    ]

    
def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-20"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-10"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-01-01"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-01-01"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-10"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-20"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-20"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-10"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-01-01"},
    ]

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid")  
