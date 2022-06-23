from flask import Flask , render_template, request
from flask_mail import Mail , Message

app = Flask(__name__)
app.config.update(
MAIL_SERVER = 'smtp.gmail.com' ,
MAIL_PORT = '465' ,
MAIL_USE_SSL  = True ,
MAIL_USERNAME = 'idrajinder9@gmail.com' ,
MAIL_PASSWORD = 'Rajinder22king')

mail = Mail(app)

@app.route('/' , methods = ['GET' , 'POST'])
def index():
     
     if(request.method == "POST" ):
         
         name =  request.form['name']
         email =  request.form['email']
         msg =  request.form['msg']
         
         mail.send_message( "New message From " + name  ,
        sender = email ,
        recipients = 'idrajinder9@gmail.com' ,
        body = msg
        
        )
         
   
         
         
         
     
         return "Message Sent Success"
         
     return render_template('mail.html' )
     
    
    

if __name__=="__main__":
    app.run(debug = True)
    

