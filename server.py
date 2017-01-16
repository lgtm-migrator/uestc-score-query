from flask import Flask,request,json,Response,jsonify
import uestc_query,os

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def home():
    username = request.args.get('username');
    password = request.args.get('password');
    score_list = uestc_query.query(username,password);
    resp = Response(response=json.dumps(score_list,ensure_ascii=False,indent=2),
                    status=200,
                    mimetype="application/json")
    return resp

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)