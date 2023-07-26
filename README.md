# README #

This api determines the valid moves for a given chess piece on a chessboard. This is a complete dockerized Flask application and can be run using the steps below.

### Running the application ###
1. Clone the repository ```valid-chess-moves```
2. Go to directory ```/valid-chess-moves```
3. Run the command ```docker-compose up -d```


### API Endpoint ###
1. The API endpoint is ```localhost:5432/chess/<slug>``` is a POST method where <slug> represents the chess piece.
2. The input to the API is provided in the request body in JSON format


### Input and Output ###
1. The API call is made to ```localhost:5432/chess/knight```
2. The input is passed in the request body in JSON format. <br>```{"positions":{"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}}```

3. The output is returned as a JSON object of valid moves.<br>```{"valid_moves":["H1", "H3", "H4", "H8", "A8"]}```

### Tests ###



#### Test Case 1 ####
INPUT:slug=Knight, positions =  {"Queen": "E7", "Bishop": "B7", "Knight": "C3", "Rook":"G5"}<br>
OUTPUT:{
  "valid_moves": ["A2",
    "A4",
    "B1",
    "D1"]}<br>
RESULT: PASS <br>
#### Test Case 3 ####
INPUT:slug = Rook, positions={"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}<br> 
OUTPUT:{
  "valid_moves": [
    "A5",
    "H1",
    "H3",
    "H4",
    "H8"
  ]
}<br>
RESULT: PASS <br>
#### Test Case 2 ####
INPUT : slug=Queen , positions= {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}<br>
OUTPUT : "valid_moves": [
    "A1",
    "B1",
    "B7",
    "C1",
    "E1",
    "F1",
    "G1",
    "H8"
  ]
} <br>
RESULT : PASS <br>

#### Test Case 4 ####
INPUT:slug=Bishop, positions =  {"Rook":"E5","Bishop": "D4", "Queen":"E3", "Knight": "C3"}<br>
OUTPUT: "valid_moves": [] <br>
RESULT: PASS <br>
