from stockfish import Stockfish

stockfish = Stockfish("stockfish")
stockfish.set_fen_position(
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq")
print(stockfish.get_best_move())
print(stockfish.get_board_visual())
