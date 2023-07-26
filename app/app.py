from flask import Flask, request, jsonify
import services


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/chess/<slug>",methods=['POST'])
def valid_moves_for_slug(slug):
    chess_piece = slug.capitalize()
    try:
        input = request.json
        if 'positions' in input :
            positions = input['positions']
        else :
            return jsonify({'error':'Invalid JSON data. Missing Parameters'}),400 
        
        pos = positions.pop(chess_piece)
        chess_board = services.get_valid_moves(positions)

        list_of_moves = services.get_moves_for_slug(chess_board,chess_piece,pos)#get_valid_moves(positions, chess_piece)
        output = {'valid_moves':[]}
        valid_moves =[]
        for moves in list_of_moves:
            valid_moves.append(chr(moves[0]+ord('A')) + str(moves[1]+1))
        output['valid_moves']=sorted(valid_moves)
        return output,200
    
    except Exception as e:
         print(e)
         return jsonify({'error':'Invalid JSON data'}),500

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5432)