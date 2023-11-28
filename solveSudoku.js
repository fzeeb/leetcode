/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
  // helper function to check if a number is valid
  function isValid(board, row, col, num) {
    for (let i = 0; i < 9; i++) {
      if (board[row][i] === num || board[i][col] === num) {
        return false;
      }
    }
    let startRow = Math.floor(row / 3) * 3;
    let startCol = Math.floor(col / 3) * 3;
    for (let i = startRow; i < startRow + 3; i++) {
      for (let j = startCol; j < startCol + 3; j++) {
        if (board[i][j] === num) {
          return false;
        }
      }
    }
    return true;
  }

  // helper function to solve sudoku
  function solve(board) {
    for (let row = 0; row < board.length; row++) {
      for (let col = 0; col < board[row].length; col++) {
        if (board[row][col] === '.') {
          for (let num = 1; num <= 9; num++) {
            if (isValid(board, row, col, num.toString())) {
              board[row][col] = num.toString();
              if (solve(board)) {
                return true;
              } else {
                board[row][col] = '.';
              }
            }
          }
          return false;
        }
      }
    }
    return true;
  }

  // call helper function to solve sudoku
  solve(board);
};