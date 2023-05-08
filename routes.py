#Necssary imports 
from Coronaweb import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, session
from Coronaweb.models import Hospital

#Home page route
@app.route('/')
@app.route('/home')
def home():
    return render_template('index1.html')

#Login page route
@app.route('/login', methods=["GET", "POST"])
def login():
    #Checking the request type 
    if request.method == 'POST':
        #Getting the email and password from the Front-end
        email = request.form['email']
        password = request.form['password']
        #Querying the database via the email
        hospital = Hospital.query.filter_by(email=email).first()
        #Checking if the entered credentials are in the database
        if hospital and bcrypt.check_password_hash(hospital.password, password):
            #Storing the email in a session as a key-value reference
            session['email'] = email
            flash("Logged in successfully!!", "success")
            return redirect(url_for('update', email=email))
        else:
            #Email and password don't match the data stored in the database
            flash("Incorrect email or password", "danger")
            return render_template("login.html")
    else:
        #This is for the "GET" request
        return render_template('login.html')

#Sign-up page route
@app.route('/sign_up', methods=['GET','POST'])
def register():
    #Checking the request type
    if request.method == 'POST':
        #Getting the data from the Front-end
        username=request.form['username']
        email=request.form['email']
        contact=request.form['contact']
        address=request.form['address']
        password=request.form['password']
        cpassword=request.form['cpassword']

        #Checking for the necessary conditions
        if password == cpassword:
            #Hashing the password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            #Creating the database entry
            hospital = Hospital(name=username, email=email, contact=contact, address=address, password=hashed_password)
            db.session.add(hospital)
            db.session.commit()
            flash("Account created successfully!", "success")
            return redirect(url_for('login'))
        else:
            #Conditional if the password and the confirm password don't match
            flash("Password and Confirm Password don't match", "danger")
            return render_template('signup.html')
       
    else:
        #This is for the "GET" request
        return render_template('signup.html')

#Resources page route
@app.route('/resources')
def resources():
    #Getting the current page for pagination
    page = request.args.get('page', 1, type=int)
    #Getting the required number of hospitals as per the paginate request
    hospitals = Hospital.query.paginate(page=page, per_page=4)
    return render_template('hospitals.html', hospitals=hospitals)

#Update page route
@app.route('/update', methods=["GET", "POST"])
def update():
    #Checking if the session has the required data
    email = session.get('email', 'no data')
    if email == 'no data':
        #Redirecting the user to the login page if the session has no data
        flash("You need to login to view this page.")
        return redirect(url_for('login'))
    else:
        #If the session has the email and the request is "POST"
        if request.method == "POST":
            #Getting the data from the Front-end
            beds=request.form['beds']
            icubeds=request.form['icubed']
            vaccine=request.form['vaccine']
            oxygen=request.form['oxygen']

            #Querying the database to find the hospital whose data has to be changed using the email as a unique key
            hosp_to_change = Hospital.query.filter_by(email=email).first()
            #Setting the data in the database
            hosp_to_change.beds = beds
            hosp_to_change.icubed = icubeds
            hosp_to_change.vaccine = vaccine
            hosp_to_change.oxygen = oxygen
            db.session.commit()
            flash("You information was updated successfully!!", "success")
            return render_template('resources_input.html')
        else:
            #This is for the "GET" request
            return render_template('resources_input.html')

#This is what happens when the user clicks on the 'logout' button
@app.route('/logout')
def logout():
    #Deleteing all the data in the session
    session.pop('email')
    return redirect(url_for('home'))


