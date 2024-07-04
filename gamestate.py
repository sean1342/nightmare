class GameState:
    def __init__(self, num_dots, line_end_dot_pairs, face_border_line_dot_pairs, faces_dots) -> None:
        self.num_dots = num_dots
        self.lines = line_end_dot_pairs
        self.faces = face_border_line_dot_pairs
        self.faces_dotss = faces_dots