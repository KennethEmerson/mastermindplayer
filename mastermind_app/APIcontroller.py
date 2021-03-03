import requests
import sys
import json

adress = "http://localhost:9000/mastermind"
new_game_command = "newgame"
evaluate_command = "evaluation"
solution_command = "solution"
guess_divider = '.'

# checks respons from API: i
#   if return code < 400: return response in JSON 
#   else system exit
def check_response(response):
  if(response.ok):
    return json.loads(response.content)
  else: return {"errorcode": response.status_code,"errorreason": response.reason}
    

# lets API create new game with custom number of pins and colors
# returns API response in JSON
def create_new_game(number_of_pins,number_of_colors):
  response = requests.get(f'{adress}/{new_game_command}/{number_of_pins}/{number_of_colors}')
  print(" response from newgame")
  return check_response(response)

# 
def evaluate_guess(guess):
  response = requests.get(f'{adress}/{evaluate_command}/{guess_divider.join(str(x) for x in guess)}')
  print(f'response in API controller to API: {response.content}')
  return check_response(response)


def get_solution():
  response = requests.get(f'{adress}/{solution_command}') 
  return check_response(response)


if __name__ == '__main__':
  print("test controller")
  content = create_new_game(4,4)
  for key in content:
          print(key + " : " + str(content[key]))
  content = (evaluate_guess((1,1,1,1)))
  if "errorcode" in content:
    print(content.get("errorreason"))
  