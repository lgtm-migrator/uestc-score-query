from flask import Flask, request, json, Response, jsonify, redirect
import uestc_query
import os

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))


@app.before_request
def before_request():
    # force https
    if os.getenv('ISCF') != None and request.headers.get('X-Forwarded-Proto') == "http":
        return redirect(request.url.replace('http://', 'https://', 1), code=301)
    # check param
    if request.args.get('username') == None or request.args.get('password') == None:
        return Response(response='param error', status=400)


@app.route('/')
def home():
    username = request.args.get('username')
    password = request.args.get('password')
    score_list = uestc_query.query(username, password)
    resp = Response(response=json.dumps(score_list, ensure_ascii=False, indent=2),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/cookie')
def get_authorized_cookie():
    username = request.args.get('username')
    password = request.args.get('password')
    cookie_jar = uestc_query.get_authorized_session_cookie(username, password)
    # maybe need modify cookie str
    if request.headers.get('Content-Type') == "application/json":
        resp = Response(response=json.dumps(cookie_jar.get_dict(), ensure_ascii=False, indent=2),
                        status=200,
                        mimetype="application/json")
    else:
        resp = ""
        for (k, v) in cookie_jar.get_dict().items():
            resp += "%s=%s; " % (k, v)
    return resp

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
