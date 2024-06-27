from flask import Flask, jsonify
import requests
import csv

app = Flask(__name__)

def fetch_todos():
    # Récupération des données depuis l'API JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur : ", response.status_code)
        return []

def save_todos_to_csv(todos, filename="todos.csv"):
    # Enregistrement des données dans un fichier CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["userId", "id", "title", "completed"])  # En-têtes
        for todo in todos:
            writer.writerow([todo["userId"], todo["id"], todo["title"], todo["completed"]])

@app.route('/', methods=['GET'])
def get_todos():
    todos = fetch_todos()
    if todos:
        save_todos_to_csv(todos)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Failed to fetch todos"}), 500

if __name__ == "__main__":
    app.run(debug=True)
