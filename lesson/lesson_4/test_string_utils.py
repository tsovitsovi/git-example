from string_utils import StringUtils


def test_capitilize():
    srting_utilitis = StringUtils()
    res= srting_utilitis.capitilize(string= "skypro")
    assert res == "Skypro"