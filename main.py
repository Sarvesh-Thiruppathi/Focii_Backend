from flask import Flask, jsonify, request
from src.block import block

app = Flask(__name__)

# Define an endpoint to get a list of items
@app.route('/verifyWebsite', methods=['POST','GET'])
def get_items():
  if (request.method == 'POST'):
    if request.is_json:
      data = request.get_json()

      print(data)
        
      if 'keywordInput' in data and 'keywordWebsite' in data:
        blockReturn = block(data['keywordInput'],data['keywordWebsite'])
        return jsonify(int(blockReturn))

        with open('requestJson.txt', 'a') as file:
          file.write(str(data) + '\n')

        return jsonify(int(blockReturn))

      return "403 Forbidden", 403

  else:
    return "405 Method Not Allowed", 405

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
