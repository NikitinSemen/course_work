from utils.utils import get_format_date
from utils.utils import mask_numb
from utils.utils import mask_number


def test_get_format_date():
    assert get_format_date("2019-09-11T17:30:34.445824") == '11-09-2019'


def test_mask_numb():
    assert mask_numb("Счет 24763316288121894080") == '**4080'


def test_mask_number():
    assert mask_number("Счет 24763316288121894080") == 'Счет 247633162881**** '
