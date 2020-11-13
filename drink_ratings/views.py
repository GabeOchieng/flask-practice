from drink_ratings import app
from flask import render_template, abort


drinks = {
    0: {
        'name': 'Black Cherry',
        'rating': 0
    },
    1: {
        'name': 'Grape',
        'rating': 10
    }
}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def hello_world():
    return "hello World"


@app.route('/drinks')
def get_drinks():
    # return jsonify({'drinks': drinks})
    return render_template("drinks.html", drinks=drinks)


@app.route('/drinks/<id>')
def get_rating(id):
    # this needs to be an int.
    # return drinks.get(int(id)) # for json
    drink = drinks.get(int(id))
    if drink is None:
        abort(404, description="Resource not found")

    return render_template("drink.html", drink=drinks.get(int(id)))