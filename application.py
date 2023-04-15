from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello, World!'

@application.route('/<username>')
def hello_user(username):
    return f'Hello, {username}!'

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    
    application.debug = True
    application.run(port=8000)


# from flask import Flask, render_template, request
# app = Flask(__name__)
# var1="CHAO"
# @app.route('/',methods = ['GET'])
# def show_index_html():
#         var1='hola'
#         return render_template('index.html', message=var1)

# @app.route('/send_data1', methods = ['POST'])
# def get_data_from_html():
#         pay = request.form['pay1']
#         var1=pay
#         #print ("Pay is " + pay)
#         #return "Data sent. Please check your program log"
         
#         return render_template('index.html',message=var1)
    
    
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000, debug=True)
    
#print(h)