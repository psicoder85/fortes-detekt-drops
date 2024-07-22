from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reports')
def reports():
    with open('data/reports/report.txt', 'r') as report_file:
        reports = report_file.readlines()
    return render_template('reports.html', reports=reports)

if __name__ == '__main__':
    app.run(debug=True)
