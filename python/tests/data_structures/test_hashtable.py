import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# ask about display?# @pytest.mark.skip("TODO")
@pytest.mark.skip("TODO")
def test_internals():  # @pytest.mark.skip

    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


# @pytest.mark.skip
def test_set():
    ht = Hashtable(10)
    ht.set("bones", 206)
    ht.set("ligaments", 900)
    assert ht._buckets[ht._hash("bones")].head.value == ["bones", 206]
    assert ht._buckets[ht._hash("ligaments")].head.value == ["ligaments", 900]


# @pytest.mark.skip
def test_get():
    ht = Hashtable()
    ht.set("whiskers", "cat")
    actual = ht.get("whiskers")
    expected = "cat"
    assert actual == expected


# @pytest.mark.skip
def test_key_return():
    ht = Hashtable()
    ht.set("Rush Hour", "Comedy")
    ht.set("Halloween", "Horror")
    ht.set("Terminator 2", "Action")
    assert ht.keys() == ["Rush Hour", "Halloween", "Terminator 2"]
    assert ht.keys() != ["Comedy", "Horror", "Action"]

# @pytest.mark.skip
def test_has():
    ht = Hashtable()
    ht.set("Shark", "fish")
    ht.set("Platypus", "mammal")
    ht.set("Boa", "reptile")
    assert ht.has("Boa") == True
    assert ht.has("Flamingo") == False


# @pytest.mark.skip
def test_hash():
    ht = Hashtable()
    assert ht._hash("Python") == 934
    assert ht._hash("Pythons") == 47
    assert ht._hash("python") != 934
