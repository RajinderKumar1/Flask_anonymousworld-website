from flask import Flask , render_template ,request , session , redirect
import json


#from flask_sqlalchemy import SQLAlchemy

#open configjson file

with open('config.json', 'r') as f :
    params = json.load(f) ["params"]


# flask intilizing 
app = Flask(__name__)

app.secret_key = 'super-secret-key'



#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/Anonymous'


#db = SQLAlchemy(app)

"""class Messages(db.Model):
    Sr_no = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Message = db.Column(db.String(100), nullable=False)"""
    

#when someone go in our / end point then show template
@app.route('/')
def home():
    
    return render_template('Index.html' , params = params)
    

# second home
@app.route('/home' )
def home2():
    
    return render_template('Index.html' ,params = params )
    

# about page
@app.route('/about.html' )
def about():
    return render_template('about.html' ,params = params )
    
 
 #log out
@app.route('/static/logout')
def logout():
     
     session.pop('user')
     return redirect('/')
     
def profile():
    
    return render_template('login.html' ,params = params )
 #profile page
@app.route('/profile.html')
def profile():
    return render_template('login.html' ,params = params )
    

    
 #contect page
 
@app.route('/contect.html' , methods = ['GET' , 'POST'])
def contect():
    if(request.method == "POST" ):
            
            
            
            #fatching data from form !
            name =  request.form['name']
            msg =  request.form['msg']
            
            # store data in file
            f = open("demo.txt","a")
            f.write(f" \n New message \n  From {name} \n Message = {msg} \n -------------------------" )
            f.close()
            return "Message sent Successfully !"
        
        #simple template render for contect page
    
    return render_template('contect.html' , params = params)
    
 
 #Login page   
@app.route('/static/Login.html' , methods = ['GET' , 'POST'])
def login():
        
        
        
        
        if (request.method == "POST" ):
             
             
             uname = request.form['uname']
             passw = request.form['upass']
             session['user']= uname
            
             if "user" in session and session['user']==params['user_name']:
                return render_template("Index.html" , params = params )
            
        
           
             if uname == params['user_name'] and passw == params['password'] :
                
                
                return render_template("Index.html" , params = params )
                
                
                
            
            
        else:
            
            return render_template('Login.html' ,params = params )   
        
            
            
        return render_template('Login.html' ,params = params )   
        
        
  #profile page      
@app.route('/static/profile.html')
def logtoprofile():
    if "user" in session and session['user']==params['user_name']:
        return render_template('logdpro.html' ,params = params )
    
    return render_template('profile.html' ,params = params )
    
 #static page lodes   
 
@app.route('/static/about.html')
def about2():
    if "user" in session and session['user']==params['user_name']:
        return render_template('about.html' ,params = params )
    return render_template('login.html' ,params = params )   

@app.route('/static/postnew')
def pro2():
   
   
   
    if "user" in session and session['user']==params['user_name']:
                
                return render_template("postnew.html" , params = params )
    return render_template('login.html' ,params = params )

@app.route('/static/Articles')
def articles2():
    return render_template('posts.html' ,params = params )
    
@app.route('/static/home')
def home3():
    return render_template('Index.html' ,params = params )
    
    


 #Articles page
@app.route('/Articles')
def post():
  f = open("post.txt","r")
  file = f.read()
  f = open("title.txt","r")
  title = f.read()
  f.close()
  
  return render_template('posts.html' , params = params , file = file , title = title )
  
# new post
@app.route('/postnew' , methods = ['GET' , 'POST'])
def newpost():
    if(request.method == "POST"):
        title = request.form['title']
        content = request.form['content']
        f = open("post.txt","w")
        f.write(f" \n      \t {content} \n \n ")
        f.close()
        f = open("title.txt","w")
        f.write(f" \n {title}  \n ")
        f.close()
        return " Posted Successfully !"
  
        
    return render_template('newlog.html' ,params = params )
    
    

        
app.run(debug = True)







    