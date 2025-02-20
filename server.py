from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection parameters (update these with your actual credentials)
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
 # Default PostgreSQL port

# Function to connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tech')
def tech():
    return render_template("tech.html")

@app.route('/nontech')
def nontech():
    return render_template("nontech.html")
# Tech Events Registration

@app.route('/cipher', methods=['GET', 'POST'])
def cipher():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']

        # Insert into PostgreSQL for Cipher event
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cipher_chase (team_name, member1_name, member1_department_and_year, member2_name, member2_department_and_year)
            VALUES (%s, %s, %s, %s, %s)
        """, (team_name, member1_name, member1_department_year, member2_name, member2_department_year))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template("cipher.html")


@app.route('/scrunch', methods=['GET', 'POST'])
def scrunch():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']

        # Insert into PostgreSQL for Scrunch event
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO scrunch_and_pick (team_name, member1_name, member1_department_and_year, member2_name, member2_department_and_year)
            VALUES (%s, %s, %s, %s, %s)
        """, (team_name, member1_name, member1_department_year, member2_name, member2_department_year))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template("scrunch.html")


@app.route('/ryz', methods=['GET', 'POST'])
def ryz():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']
        member3_name = request.form['member3_name']
        member3_department_year = request.form['member3_department_and_year']

        # Insert into PostgreSQL for Ryz-n-Fall event
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ryz_n_fall (team_name, member1_name, member1_department_and_year, member2_name, member2_department_and_year,member3_name, member3_department_and_year)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (team_name, member1_name, member1_department_year, member2_name, member2_department_year,member3_name, member3_department_year))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template("ryz.html")

# Non-Tech Events Registration

@app.route('/booth', methods=['GET', 'POST'])
def booth():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']

        # Insert into PostgreSQL for The Booth event
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO booth (team_name, member1_name, member1_department_and_year, member2_name, member2_department_and_year)
            VALUES (%s, %s, %s, %s, %s)
        """, (team_name, member1_name, member1_department_year, member2_name, member2_department_year))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template("booth.html")


@app.route('/dalgona', methods=['GET', 'POST'])
def dalgona():
    if request.method == 'POST':
      
        member1_name = request.form['player_name']
        member1_department_year = request.form['department_and_year']
        

        # Insert into PostgreSQL for Dalgona Candy event
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dalgona (player_name, department_and_year)
            VALUES (%s, %s)
        """, ( member1_name, member1_department_year, ))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template("dalgona.html")


@app.route('/moviemania', methods=['GET', 'POST'])
def moviemania():
    if request.method == 'POST':
        team_name = request.form['team_name']
        member1_name = request.form['member1_name']
        member1_department_year = request.form['member1_department_and_year']
        member2_name = request.form['member2_name']
        member2_department_year = request.form['member2_department_and_year']
        member3_name = request.form['member3_name']
        member3_department_year = request.form['member3_department_and_year']

        # Insert into PostgreSQL for Moviemania event
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO moviemania (team_name, member1_name, member1_department_and_year, member2_name, member2_department_and_year, member3_name, member3_department_and_year)
            VALUES (%s, %s, %s, %s, %s,%s, %s)
        """, (team_name, member1_name, member1_department_year, member2_name, member2_department_year, member3_name, member3_department_year))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template("moviemania.html")

if __name__ == "__main__":
    app.run(debug=True)
