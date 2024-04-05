from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Function to fetch data from SQL Server database
def fetch_data():
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=ERVERRENEW01;'
                          'DATABASE=everrenew;'
                          'UID=sa;'
                          'PWD=P@55w0rd')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.Communication")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# Route to render the HTML template with fetched data
@app.route('/')
def display_data():
    data = fetch_data()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=False)
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change the port number as needed