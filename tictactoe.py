import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", layout="centered")

# Inisialisasi session state
if 'board' not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.game_over = False

def check_winner(board):
    # Cek baris dan kolom
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    # Cek diagonal
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_draw(board):
    for row in board:
        if "" in row:
            return False
    return True

st.title("🎮 Tic Tac Toe - Streamlit Version")
st.subheader(f"Pemain saat ini: {st.session_state.current_player}")

if st.session_state.winner:
    st.success(f"Pemain {st.session_state.winner} menang! 🎉")
elif st.session_state.game_over:
    st.warning("Permainan seri 🤝")

# Tampilkan papan
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell_value = st.session_state.board[i][j]
        if cols[j].button(cell_value if cell_value else " ", key=f"{i}{j}", disabled=bool(cell_value) or st.session_state.winner):
            if not st.session_state.game_over:
                st.session_state.board[i][j] = st.session_state.current_player
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                    st.session_state.game_over = True
                elif is_draw(st.session_state.board):
                    st.session_state.game_over = True
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Tombol reset
if st.button("🔄 Mulai Ulang"):
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.game_over = False
