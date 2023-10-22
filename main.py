from flask import Flask, jsonify, request
from block import block

app = Flask(__name__)

# Define an endpoint to get a list of items
@app.route('/verifyWebsite', methods=['POST','GET'])
def get_items():
  if (request.method == 'POST'):
    if request.is_json:
      data = request.get_json()

      print(data)
        
      if 'keywordsInput' in data and 'keywordWebsite' in data:
        return block(data['keywordsInput'],data['keywordWebsite'])

      return "SOMETHING WENT WRONG"
      print(data)

  else:
    return "405 Method Not Allowed", 405

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
