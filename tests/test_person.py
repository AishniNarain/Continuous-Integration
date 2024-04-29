from beings.person import Person
import pytest

@pytest.fixture
def person():
    return Person("Aishni Narain", 23, jobs = ["Software Engineer"])

def test_init(person : Person):
    assert person.name == "Aishni Narain"
    assert person.age == 23
    assert person.jobs == ["Software Engineer"]
    
def test_forename(person : Person):
    assert person.forename == "Aishni"
    
def test_surname(person : Person):
    assert person.surname == "Narain"
    
def test_no_surname(person : Person):
    person.name = "Ethan"
    assert not person.surname
    
def test_celebrate_birthday(person : Person):
    person.celebrate_birthday()
    assert person.age == 24
    
def test_add_job(person : Person):
    person.add_job("Analyst")
    assert person.jobs == ["Software Engineer","Analyst"]