#include <iostream>
#include <map>
#include <vector>
using namespace std;
typedef unsigned long long ll;
typedef vector<vector<bool>> Board;

const int height = 42;
const int width = 42;

const int di[] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dj[] = {-1, 0, 1, -1, 1, -1, 0, 1};

void step(Board &board, Board &tmp) {
  for (int i = 0; i < height; ++i) {
    for (int j = 0; j < width; ++j) {
      int count = 0;
      for (int k = 0; k < 8; ++k) {
        int ni = (i + di[k] + height)%height;
        int nj = (j + dj[k] + width)%width;
        count += board[ni][nj];
      }
      tmp[i][j] = (count == 3 || (count == 2 && board[i][j]));
    }
  }
  swap(board, tmp);
}

int main() {
  Board board(height, vector<bool>(width));
  Board tmp(board);
  for (int i = 0; i < height; ++i) {
    for (int j = 0; j < width; ++j) {
      char c; cin >> c;
      board[i][j] = (c == '1');
    }
  }

  map<Board, int> seen {{board, 0}};
  int cycle_turn = -1;
  int cycle_length = -1;
  for (int turn = 1; cycle_turn == -1; ++turn) {
    step(board, tmp);
    auto it = seen.find(board);
    if (it == seen.end()) {
      seen[board] = turn;
    } else {
      cycle_turn = it->second;
      cycle_length = turn - cycle_turn;
    }
  }
  cout << "Cycle starts at: " << cycle_turn << endl;
  cout << "Cycle length is: " << cycle_length << endl;
  cout << "The answer is " << cycle_turn << "-" << cycle_length << endl;
}

