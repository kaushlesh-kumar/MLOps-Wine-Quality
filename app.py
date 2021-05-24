from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
#from prediction_service import prediction

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        try:
            if request.form:    #if request is coming from the webapp
                dict_req = dict(request.form).values()
                dict_req = [list(map(float, dict_req))]
                #response = prediction.form_response(dict_req)
                response = predict(dict_req)
                return render_template("index.html", response=response)
            elif request.json:  #if request is from any api testing app (postman)
                #response = prediction.api_response(request.json)
                response = api_response(request)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Please try again!"}
            error = {"error": e}

            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response":response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Something went wrong!! Please try again!"}
        return error


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
