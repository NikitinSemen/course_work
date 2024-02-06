import os.path

from utils.utils import get_data_json, get_new_operation, get_sort_operation, get_five_operation


def test_get_data_json():
    file_path = os.path.dirname(__file__)
    json_data = get_data_json(os.path.join(file_path, "file.json"))
    assert isinstance(json_data, list)
    assert isinstance(json_data[0], dict)


def test_get_new_operation():
    data = [
        {
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
        },
        {
            "state": "EXECUTED",
        },
        {
            "state": "CANCELED",
        }
    ]

    expected_data = [
        {
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
        },
    ]
    assert get_new_operation(data) == expected_data


def test_get_sorted_operation():
    data = [
        {
            "date": "2018-04-14T19:35:28.978265",
        },
        {
            "date": "2019-09-11T17:30:34.445824",
        }
    ]

    expected_data = [
        {
            "date": "2019-09-11T17:30:34.445824",
        },
        {
            "date": "2018-04-14T19:35:28.978265",
        },
    ]
    assert get_sort_operation(data) == expected_data


def test_get_five_operation():
    data = [1, 2, 3, 4, 5, 6, 7]
    expected_data = [1, 2, 3, 4, 5]
    assert get_five_operation(data) == expected_data


