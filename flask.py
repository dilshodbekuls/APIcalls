#pip  install flask
from flask import Flask, jsonify, request, make_response

app = Flask(_name_)

businesses = [
    {
        "id": 1,
        "Name": "Ruchira Tex",
        "Location": "Gravesend",
        "Ratings": "5",
        "Reviews": []
    },
    {
        "id": 2,
        "Name": "Ruwani Tex",
        "Location": "Farringdon",
        "Ratings": "5",
        "Reviews": []
    },
    {
        "id": 3,
        "Name": "Ravindu Tex",
        "Location": "London",
        "Ratings": "5",
        "Reviews": []
    }
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to COM661"})

@app.route('/businesses', methods=['GET'])
def get_all_businesses():
    return make_response(jsonify({"businesses": businesses}), 200)

@app.route("/businesses", methods=['POST'])
def add_business():
    data = request.form
    new_id = businesses[-1]["id"] + 1 if businesses else 1
    new_business = {
        "id": new_id,
        "Name": data.get("Name"),
        "Location": data.get("Location"),
        "Ratings": data.get("Ratings", "0"),
        "Reviews": []
    }
    businesses.append(new_business)
    return make_response(jsonify(new_business), 200)

@app.route("/businesses/<int:biz_id>", methods=['GET'])
def get_one_id_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            return make_response(jsonify(biz), 200)
    return make_response(jsonify({"error": "Not found"}), 404)

@app.route("/businesses/<int:biz_id>", methods=['PUT'])
def edit_business(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"] == biz_id:
            biz["Name"] = data.get("Name")
            biz["Location"] = data.get("Location")
            biz["Ratings"] = data.get("Ratings")
            break
            
    return make_response(jsonify(biz), 200)
    
@app.route("/businesses/<int:biz_id>", methods=['DELETE'])
def delete_business(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"] == biz_id:
          businesses.remove(biz)
          break    
    return make_response(jsonify(biz), 200)



@app.route("/businesses/<int:biz_id>/review", methods=['GET']) 
def get_all_reviews(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"] == biz_id:
          break
        return make_response(jsonify(biz["review"]), 200)


@app.route("/businesses/<int:biz_id>/reviews", methods=['PUT'])
def add_new_review(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"] == biz_id:
            if len(biz["review"]) == 0:
                new_review_id =1
            else:
                new_review_id +biz["review"][-1]["id"]+1
            new_review = {
                "id": new_review_id,
                 "Name": data.get("Name"),
                 "comment": data.get("comment"),
                 "star": data.get("star"),
                 "Reviews": []
            }
            biz["review"].append(new_review)
            break
   
        return make_response(jsonify(new_review),200)

if _name_ == '_main_':
    app.run(debug=True)


#python week2.py