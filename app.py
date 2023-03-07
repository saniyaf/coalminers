
from flask import Flask, render_template , request,session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import pymysql
pymysql.install_as_MySQLdb()
import json 

with open('config.json' , 'r') as C:
    params = json.load(C)["params"]
local_Server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

 

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT =   '464',
    MAIL_USE_SSL = 'True',
    MAIL_USERNAME = 'saniyaxfatima2409@gmail.com',
    MAIL_PASSWORD = 'exqoickczhrhfpfu'
)


mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/coalminers'
db = SQLAlchemy(app)

# class contact(db.Model):
#     sno=db.Column(db.Integer , primary_key = True)
#     name=db.Column(db.String(80) , nullable = False)
#     email=db.Column(db.String(80), nullable = False)
#     address=db.Column(db.String(80) , nullable = False)
#     city=db.Column(db.String(80) , nullable = False)
#     jobtitle=db.Column(db.String (80), nullable = False)
#     exp=db.Column(db.String (80), nullable = False)
#     phone_num=db.Column(db.String(80) , nullable = False)
#     start_date=db.Column(db.Date , nullable = False)
#     cv=db.Column(db.String(80) , nullable = False)
#     date=db.Column(db.Date , nullable = True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog-details')
def blog_details():
    return render_template('blog-details.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/project-details')
def project_details():
    return render_template('project-details.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/service-details')
def service_details():
    return render_template('service-details.html')




@app.route('/contact', methods = {'GET','POST'})
def contact():
    if  request.method == 'POST':
        # firstname = request.form.get('firstname')
        email = request.form.get('email')
        # address = request.form.get('address')
        # city = request.form.get('city')
        # title = request.form.get('title')
        # experience = request.form.get('experience')
        # phone = request.form.get('phone')
        # date = request.form.get('date')
        # entry = contact( name = firstname,
        #                      email = email,
        #                      address = address,
        #                      city = city,
        #                      jobtitle = title,
        #                      exp = experience,
        #                      phone_num = phone,
        #                      start_date = date )

        # db.session.add(entry)
        # db.session.commit()
        mail.send_message( 'new quary from',
                              sender = email,
                              recipients = [params['gmail_user']],
                              body = "Hello"
        )
        
    return render_template('contact.html', params= params)
        

@app.route('/services')
def services():
    return render_template('services.html')



if __name__== "__main__":
    app.run(debug=True)


