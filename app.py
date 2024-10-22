from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="192.168.1.127",  # Replace with VM IP
        database="k8sappdb",
        user="k8sappuser",
        password="k8spass"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Connected to PostgreSQL: {db_version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
