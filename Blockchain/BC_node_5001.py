from Blockchain_DAPP import Blockchain
from flask import Flask, jsonify, request

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine_block',methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof,previous_hash)
    response = {
        'message':'block is mined',
        'index':block['index'],
        'timestamp':block['timestamp'],
        'proof':block['proof'],
        'previous_hash':block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/get_chain',methods=['GET'])
def get_chain():
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/is_valid',methods=['GET'])
def is_valid():
    is_valid=blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message':'Your chain is validated'}
    else:
        response = {'message':'Your chain is not valid'}
    return jsonify(response), 200

@app.route('/add_transaction',methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender','receiver','amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements are missing', 400
    index = blockchain.add_transaction(
        json['sender'],
        json['receiver'],
        json['amount']
    )
    response = {'Message':f'The transaction is added to block {index}'}
    return jsonify(response), 201

@app.route('/connect_nodes',methods=['POST'])
def connect_nodes():
    json = request.get_json()
    nodes = json.get('nodes')
    print(nodes)
    if nodes is None:
        return 'No Nodes', 400
    for node in nodes:
        blockchain.add_node(node)
    response = {
        'message': 'all nodes are now connected',
        'Total nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201
    
@app.route('/replace_chain',methods=['GET'])
def replace_chain():
    is_chain_replace = blockchain.replace_chain()
    if is_chain_replace:
        response = {
            'message': 'chain replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'chain not replaced',
            'new_chain': blockchain.chain
        }
    return jsonify(response), 201

app.run(host='127.0.0.1',port = 5001)