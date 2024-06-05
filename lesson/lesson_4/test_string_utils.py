from string_utils import StringUtils
import pytest

def test_capitilize():
    srting_utilitis = StringUtils()
    res= srting_utilitis.capitilize(string= "skypro")
    assert res == "Skypro"

def test_capitilize_nonText():
    srting_utilitis = StringUtils()
    res= srting_utilitis.capitilize(string= "")
    assert res == ""


def test_trim():
    srting_utilitis = StringUtils()
    res= srting_utilitis.trim(string= "   skypro")
    assert res == "skypro"






def test_to_list():
    srting_utilitis = StringUtils()
    res= srting_utilitis.to_list(string= "a,b,c,d")
    assert res == ["a", "b", "c", "d"]

def test_to_list():
    srting_utilitis = StringUtils()
    res= srting_utilitis.to_list(string= "a,b,c,d")
    assert res == ["a", "b", "c", "d"]