from flask import Flask, render_template, request, jsonify
import APIcontroller


def create_app():
    """creates the Flask app"""
    app = Flask(__name__)

    @app.route("/")
    def home():
        """returns the rendered Mastermind interface webpage"""

        print("page loaded")
        return render_template('layouts/panel.html')


    @app.route('/newGame', methods=['POST'])
    def newGame():
        """process the AJAX request to start a new game"""

        number_of_pins = request.form['numberOfPins']
        number_of_colors = request.form['numberOfColors']

        if number_of_pins > 0 and number_of_colors > 0:
            return APIcontroller.create_new_game(number_of_pins,number_of_colors)
        else: return jsonify({'error':'missing data'})


    @app.route('/evaluate',methods=['POST'])
    def evaluate():
        """process the AJAX request to evaluate the guess"""
        
        # string needs to be converted to a tuple
        guess = tuple(request.form['guess'].replace(".",",").split(","))
        
        if guess:
            temp = APIcontroller.evaluate_guess(guess)
            return temp
        else:
            return jsonify({'error':'missing data'})


    @app.route('/solution',methods=['POST'])
    def solution():
        """process the AJAX request to send the solution"""
        
        return APIcontroller.get_solution()
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()