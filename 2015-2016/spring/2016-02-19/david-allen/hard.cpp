
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

const int BOARD_LENGTH = 4;
const char PLAYER_1_SYMBOL = 'X';
const char PLAYER_2_SYMBOL = 'O';
const char FREE_SYMBOL = 'T';
const char DRAW = 'D';
const char INCOMPLETE_SYMBOL = '.';
const string CASE_1_OUTPUT = "X won";
const string CASE_2_OUTPUT = "O won";
const string CASE_3_OUTPUT = "Draw";
const string CASE_4_OUTPUT = "Game has not completed"; 

char computeWinner( string [] );

int main(int argc, char* argv[]) {

	int board_quantity;
	int board_count;
	string board[ BOARD_LENGTH ];
	char win_char;

	ifstream test_file;
	test_file.open(argv[1]);
	string file_line;

	if ( test_file.is_open() ) {
		getline( test_file, file_line );
		istringstream (file_line) >> board_quantity;
		for (int board_count = 0; board_count < board_quantity; board_count++) {
			for (int row_count = 0; row_count < BOARD_LENGTH; row_count++) {
				getline( test_file, board[row_count] );
			}
			getline ( test_file, file_line ); // get blank line

			win_char = computeWinner(board);
			cout << "Case #";
			switch ( win_char ) {
				case PLAYER_1_SYMBOL:
					cout << "1:\t" << CASE_1_OUTPUT << endl;
					continue;
				case DRAW:
					cout << "2:\t" << CASE_3_OUTPUT << endl;
					continue;
				case INCOMPLETE_SYMBOL:
					cout << "3:\t" << CASE_4_OUTPUT << endl;
					continue;
				case PLAYER_2_SYMBOL:
					cout<< "4:\t" << CASE_2_OUTPUT << endl;
					continue;
				default:
					cout << "ERROR in computeWinner" << endl;
			}
		}
	}

	test_file.close();
	return 0;
}

char computeWinner( string board[ BOARD_LENGTH ] ) {
	const int FORWARD_DIAG = BOARD_LENGTH*2;
	const int BACKWARD_DIAG = BOARD_LENGTH*2 + 1;
	bool game_completed = true; // default
	bool win_cond_eliminated[ BOARD_LENGTH*2 + 2 ] = {false}; // rows, columns, diagonals
	char win_char;


	// rows
	for (int row = 0; row < BOARD_LENGTH; row++) {
		win_char = board[row][0];
		for (int col = 0; col < BOARD_LENGTH; col++) {
			if ( board[row][col] == INCOMPLETE_SYMBOL ) {
				win_cond_eliminated[row] = true;
				game_completed = false;
				
			}
			if ( ( board[row][col] != win_char ) 
				&& (board[row][col] != FREE_SYMBOL) ){
				win_cond_eliminated[row] = true;
			}
		}
		if ( (win_cond_eliminated[row] == false)
			&& (win_char != INCOMPLETE_SYMBOL) ) {
			return win_char;
		}
	}

	// columns
	for (int col = 0; col < BOARD_LENGTH; col++) {
		win_char = board[0][col];
		for (int row = 1; row < BOARD_LENGTH; row++) {
			if ( board[row][col] == INCOMPLETE_SYMBOL ) {
				win_cond_eliminated[BOARD_LENGTH + col] = true;
				game_completed = false;
				
			}
			if ( (board[row][col] != win_char ) 
				&& (board[row][col] != FREE_SYMBOL) ) {
				win_cond_eliminated[BOARD_LENGTH + col] = true;
			}
		}
		if ( (win_cond_eliminated[BOARD_LENGTH + col] == false)
			&& (win_char != INCOMPLETE_SYMBOL) ) {
			return win_char;
		}
	}

	// diagonals
	win_char = board[0][0];
	for (int diag = 1; diag < BOARD_LENGTH; diag++) {
		if ( board[diag][diag] == INCOMPLETE_SYMBOL ) {
			game_completed = false;
			win_cond_eliminated[FORWARD_DIAG] = true;
		}
		if ( (board[diag][diag] != win_char ) 
			&& (board[diag][diag] != FREE_SYMBOL) ) {
			win_cond_eliminated[FORWARD_DIAG] = true;
		}
	}
	if ( (win_cond_eliminated[ FORWARD_DIAG ] == false) 
		&& (win_char != INCOMPLETE_SYMBOL) ) {
		return win_char;
	}

	//
	win_char = board[BOARD_LENGTH-1][BOARD_LENGTH-1];
	for (int diag = BOARD_LENGTH-1; diag > 0; diag--) {
		if ( board[diag][BOARD_LENGTH-1 - diag] == INCOMPLETE_SYMBOL ) {
			win_cond_eliminated[BACKWARD_DIAG] = true;
			game_completed = false;
		}
		if ( (board[diag][BOARD_LENGTH-1 - diag] != win_char )
			&& (board[diag][BOARD_LENGTH-1 - diag] != FREE_SYMBOL) ) {
			win_cond_eliminated[BACKWARD_DIAG] = true;
		} 
	}
	if ( (win_cond_eliminated[ BACKWARD_DIAG ] == false)
		&& (win_char != INCOMPLETE_SYMBOL) ) {
		return win_char;
	}

	if ( game_completed ) {
		return DRAW;
	} else {
		return INCOMPLETE_SYMBOL;
	}
}
