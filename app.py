from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data
data_table = [
    {"id": 1, "company": "derm", "amount": 4100.00, "payment_date": "09/26/2023", "status": "paid", "due_date": "01/15/2024"},
    {"id": 2, "company": "derm", "amount": 4100.00, "payment_date": "10/12/2023", "status": "paid", "due_date": "01/15/2024"},
    {"id": 3, "company": "tek", "amount": 15200.00, "payment_date": "06/09/2023", "status": "paid", "due_date": "06/15/2023"},
    {"id": 4, "company": "tek", "amount": 15200.00, "payment_date": "07/12/2023", "status": "paid", "due_date": "09/15/2023"},
    {"id": 5, "company": "tek", "amount": 11400.00, "payment_date": "08/11/2023", "status": "paid", "due_date": "09/15/2023"},
    {"id": 6, "company": "tek", "amount": 14440.00, "payment_date": "09/21/2023", "status": "paid", "due_date": "01/15/2024"},
    {"id": 7, "company": "tek", "amount": 15200.00, "payment_date": "10/18/2023", "status": "paid", "due_date": "01/15/2024"},
    {"id": 8, "company": "tek", "amount": 23520.00, "status": "unpaid", "due_date": "01/15/2024"},
    {"id": 9, "company": "tek", "amount": 16800.00, "status": "unpaid", "due_date": "01/15/2024"},
    {"id": 10, "company": "tek", "amount": 16800.00, "status": "unpaid", "due_date": "01/15/2024"},
    {"id": 11, "company": "tek", "amount": 16800.00, "status": "unpaid", "due_date": "01/15/2024"}
]

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch summary data based on due date
@app.route('/summary', methods=['GET'])
def summary():
    due_date = request.args.get('due_date')
    filtered_data = [row for row in data_table if row.get('due_date') == due_date]
    total_amount = sum(row['amount'] for row in filtered_data)
    tax_rate = float(request.args.get('tax_rate'))
    tax_due = total_amount * tax_rate
    return jsonify({
        'data': filtered_data,
        'total_amount': total_amount,
        'tax_rate': tax_rate,
        'tax_due': tax_due
    })

if __name__ == '__main__':
    app.run(debug=True)
