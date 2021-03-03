from flask import Flask, render_template, request, jsonify
import APIcontroller


def create_app():
    app = Flask(__name__)

    # returns Mastermind interface panel
    @app.route("/")
    def home():
        print("page loaded")
        return render_template('layouts/panel.html')


    # AJAX request to start a new game
    @app.route('/newGame', methods=['POST'])
    def newGame():
        
        number_of_pins = request.form['numberOfPins']
        number_of_colors = request.form['numberOfColors']

        if number_of_pins and number_of_colors:
            return APIcontroller.create_new_game(number_of_pins,number_of_colors)
        else: return jsonify({'error':'missing data'})


    # AJAX request to evaluate the guess
    @app.route('/evaluate',methods=['POST'])
    def evaluate():
        # string needs to be converted to a tuple
        guess = tuple(request.form['guess'].replace(".",",").split(","))
        
        if guess:
            temp = APIcontroller.evaluate_guess(guess)
            return temp
        else:
            return jsonify({'error':'missing data'})

    # AJAX request to send the solution
    @app.route('/solution',methods=['POST'])
    def solution():
        
        return APIcontroller.get_solution()
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()