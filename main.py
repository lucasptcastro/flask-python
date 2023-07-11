from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"

@app.route("/employees/create", methods=["POST"])

# GET ALL
@app.route("/employees/getall", methods=['GET'])
def get_employees():
    return "Colaboradores"

# GET
@app.route("/employees/get", methods=['GET'])
def get_employee():
    return "Colaborador"

# DELETE
@app.route("/employees/delete", methods=["DELETE"])
def delete_employee():
    return "Colaborador excluído!"

# UPDATE
@app.route("/employees/update", methods=["UPDATE"])
def update_employee():
    return "Colaborador atualizado!"



# Hot reload
if __name__ == "__main__":
    app.run(debug=True)