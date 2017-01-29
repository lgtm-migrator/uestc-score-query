from flask import Flask,request,json,Response,jsonify,redirect,session
import uestc_query,os,uuid

app = Flask(__name__)


app.secret_key = uuid.uuid4().bytes

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

query_sessions = {}

# force https
@app.before_request
def before_request():
    if os.getenv('ISCF') != None and request.headers.get('x_forwarded_proto') == "http":
        return redirect(request.url.replace('http://', 'https://', 1), code=301)
    if "sid" not in session :
        session["sid"] = uuid.uuid4().bytes
        session["is_login"] = False
        query_sessions[session["sid"]] = uestc_query.Session()

@app.route('/sid')
def sid():
    return str(session['sid'])

@app.route('/login')
def login():
    username = request.args.get('username');
    password = request.args.get('password');
    if username != None and password != None: 
        s = query_sessions[session['sid']]
        if s.login(username,password) == True:
            session["is_login"] = True
            return Response(response="authorized success")
        else: 
            return Response(response="authorize failed",status=401)
    return Response(response="bad request", status=400)

@app.route('/grades')
def grades_list():
    if session["is_login"]:
        score_list = query_sessions[session["sid"]].get_all_grades();
        resp = Response(response=json.dumps(score_list,ensure_ascii=False,indent=2),
                status=200,
                mimetype="application/json") 
        return resp
    else :
        return Response(response="not authorized", status=401)

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)