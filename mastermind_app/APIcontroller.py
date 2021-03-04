import requests
import sys
import json


adress = "http://localhost:9000/mastermind" # the adress of the Docker container port
new_game_command = "newgame"
evaluate_command = "evaluation"
solution_command = "solution"
guess_divider = '.'


def check_response(response):
  """checks the response from the API"""

  if(response.ok):
    return json.loads(response.content)
  else: return {"errorcode": response.status_code,"errorreason": response.reason}
    

def create_new_game(number_of_pins,number_of_colors):
  """send a request to the API to start a new game"""

  response = requests.get(f'{adress}/{new_game_command}/{number_of_pins}/{number_of_colors}')
  print(" response from newgame")
  return check_response(response)


def evaluate_guess(guess):
  """send a request to the API to evaluate the guess"""

  response = requests.get(f'{adress}/{evaluate_command}/{guess_divider.join(str(x) for x in guess)}')
  print(f'response in API controller to API: {response.content}')
  return check_response(response)


def get_solution():
  """send a request to the API to get the solution"""
  
  response = requests.get(f'{adress}/{solution_command}') 
  return check_response(response)
  