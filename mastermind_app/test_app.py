#from flask import jsonify
import pytest
import json

import app as MMapp

@pytest.fixture
def client():
    app = MMapp.create_app()
    app.config["DEBUG"] = True
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_interface(client):
    result = client.get("/")
    assert result.status_code == 200

# ----------------------------------------------------------------

def test_new_game_contains_numberOfGuesses(client): 
    result = client.post("/newGame", data = {'numberOfPins':4,'numberOfColors':4})
    assert result.status_code == 200
    assert (result.json.get('numberOfGuesses')==0)

def test_new_game_contains_codeLength(client): 
    result = client.post("/newGame", data = {'numberOfPins':4,'numberOfColors':4})
    assert result.status_code == 200
    assert (result.json.get('codeLength')==4)

# TODO: add extra tests for wrong inputs

# ----------------------------------------------------------------

def test_evaluate_contains_numberOfGuesses(client): 
    result = client.post("/newGame", data = {'numberOfPins':4,'numberOfColors':4})
    result = client.post("/evaluate", data = {'guess':'1.1.1.1'})
    assert (result.json.get('numberOfGuesses')==1)

def test_evaluate_contains_correct(client): 
    result = client.post("/newGame", data = {'numberOfPins':4,'numberOfColors':4})
    result = client.post("/evaluate", data = {'guess':'1.1.1.1'})
    assert result.status_code == 200
    assert ('correct' in result.json)
    assert (isinstance(result.json.get('correct'), int))

def test_evaluate_contains_wrongPlace(client): 
    result = client.post("/newGame", data = {'numberOfPins':4,'numberOfColors':4})
    result = client.post("/evaluate", data = {'guess':'1.1.1.1'})
    assert result.status_code == 200
    assert (isinstance(result.json.get('wrongPlace'), int))

# TODO: add extra tests for wrong inputs

# ----------------------------------------------------------------

def test_solution_contains_numberOfGuesses(client):
    result = client.post("/solution")
    assert result.status_code == 200
    assert ('numberOfGuesses' in result.json)
    assert (isinstance(result.json.get('numberOfGuesses'), int))
    assert (result.json.get('numberOfGuesses')>=0)

def test_solution_contains_solution(client):
    result = client.post("/solution")
    assert ('solution' in result.json)
    assert (isinstance(result.json.get('solution'), list))
    assert (isinstance(result.json.get('solution')[0], int))

# TODO: add extra tests for wrong inputs