from flask import Flask,jsonify,make_response,request
from flask_cors import CORS,cross_origin
from descope import REFRESH_SESSION_TOKEN_NAME,SESSION_TOKEN_NAME, DescopeClient

app=Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    return "Hello World,public information"


cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/protected',methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def protected_assets():
    session_token=request.headers["Authorization"].split(" ")[1]
    try:
        descope_client=DescopeClient(project_id="P2fTyYnwJCDv2IWOZb3hoFVCGB24")
        descope_client.validate_session(session_token=session_token)
        print('Successful validation')
        response=make_response(jsonify({
            "message":"Secret Code is: Descope Rocks","serverity":"danger"
        }),
        200,)
        response.headers["Content-Type"]="application/json"
        return response
    except:
        print("Validation Failed")
        response=make_response(jsonify({
            "message":"Not Allowed","serverity":"danger"
        }),
        401,)
        response.headers["Content-Type"]="application/json"
        return response
    
if __name__=="__main__":
    app.run(port=8080)


