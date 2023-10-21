from flask import Flask, jsonify, request

app = Flask(__name__)

# Define an endpoint to get a list of items
@app.route('/verifyWebsite', methods=['POST','GET'])
def get_items():
  if (request.method == 'POST'):
    if request.is_json:
      content = request.get_json()

      print(content)
      
      return jsonify(1)

  else:
    return "ERROR 401: Unauthorized access"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
