<<<<<<< HEAD
from flask import Flask, render_template, request
from models import menu  # Import the menu from models.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        order = request.form.to_dict()  # Get the form data
        total = 0
        order_summary = {}
        
        for item in menu:
            quantity = order.get(item.name, '0')  # Get quantity for the specific item
            if quantity.isdigit() and int(quantity) > 0:  # Check if quantity is a valid integer
                order_summary[item.name] = {
                    "quantity": int(quantity),
                    "price": item.price * int(quantity)
                }  # Store valid orders with quantity and price
                total += item.price * int(quantity)  # Calculate total cost
        
        return render_template('order_summary.html', order=order_summary, total=total)

    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, render_template, request
from models import menu  # Import the menu from models.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        order = request.form.to_dict()  # Get the form data
        total = 0
        order_summary = {}
        
        for item in menu:
            quantity = order.get(item.name, '0')  # Get quantity for the specific item
            if quantity.isdigit() and int(quantity) > 0:  # Check if quantity is a valid integer
                order_summary[item.name] = {
                    "quantity": int(quantity),
                    "price": item.price * int(quantity)
                }  # Store valid orders with quantity and price
                total += item.price * int(quantity)  # Calculate total cost
        
        return render_template('order_summary.html', order=order_summary, total=total)

    return render_template('index.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 7b2ce7ad49716338a279d2b663b7f8d2202b2b3e
