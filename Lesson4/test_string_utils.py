import pytest
from string_utils import StringUtils
utils = StringUtils()
# capitilize
def test_capitilize():
	#positive
	assert utils.capitilize("skypro") == "Skypro"
	assert utils.capitilize("test") == "Test"
	#negative
	assert utils.capitilize("") == ""
	assert utils.capitilize(" ") == " "
# trim
def test_trim():
	#positive
	assert utils.trim(" skypro") == "skypro"
	assert utils.trim("  test  ") == "test  "
	assert utils.trim("   HELLO") == "HELLO"
	#negative
	assert utils.trim("") == ""
#to_list
def test_to_list():
	#positive
	assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
	assert utils.to_list("1,2,3,4") == ["1", "2", "3", "4"]
	#negative
	assert utils.to_list("", None) == []
#contains
def test_contains():
	#positive
	assert utils.contains("Test" , "e") == True
	assert utils.contains("Hello", "o") == True
	#negative
	assert utils.contains("Skypro", "A") == False
	assert utils.contains("123", "d") == False
	assert utils.contains("Привет", "2") == False
#delete_symbol
def test_delete_symbol():
	#positive
	assert utils.delete_symbol("SkyPro", "k") == "SyPro"
	assert utils.delete_symbol("Hello", "He") == "llo"
	assert utils.delete_symbol("1234567", "567") == "1234"
	assert utils.delete_symbol("Good morning", " ") == "Goodmorning"
	#negative
	assert utils.delete_symbol("Привет", "123") == "Привет"
	assert utils.delete_symbol("123456789", "ASD") == "123456789"
#starts_with
def test_starts_with():
	#positive
	assert utils.starts_with("Test" , "T") == True
	assert utils.starts_with("Sky" , "S") == True
	assert utils.starts_with("12345" , "1") == True
	#negative
	assert utils.starts_with("Test" , "E") == False
	assert utils.starts_with("234", "4") == False
	assert utils.starts_with("Привет", "1") == False
#end_with
def test_end_with():
	#positive
	assert utils.end_with("Test" , "t") == True
	assert utils.end_with("Skypro" , "o") == True
	assert utils.end_with("12345" , "5") == True
	#negative
	assert utils.end_with("123456", "5") == False
	assert utils.end_with("Skypro" , "y") == False
#is_empty
def test_is_empty():
	#positive
	assert utils.is_empty("") == True
	#negative
	assert utils.is_empty("Hello") == False
#list_to_string
def test_list_to_string():
	#positive
	assert utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4" 
	assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
	#negative
	assert utils.list_to_string([], None) == ("")