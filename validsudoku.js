/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  // initialize row, column, and box sets
  let row = new Set();
  let column = new Set();
  let box = new Set();

  // loop through rows
  for (let i = 0; i < board.length; i++) {
    // loop through columns
    for (let j = 0; j < board[i].length; j++) {
      // if cell is not empty
      if (board[i][j] !== '.') {
        // calculate box index
        let boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
        // if row, column, or box already has value, return false
        if (row.has(`${i}-${board[i][j]}`) || column.has(`${j}-${board[i][j]}`) || box.has(`${boxIndex}-${board[i][j]}`)) {
          return false;
        }
        // add value to row, column, and box
        row.add(`${i}-${board[i][j]}`);
        column.add(`${j}-${board[i][j]}`);
        box.add(`${boxIndex}-${board[i][j]}`);
      }
    }
  }
  // return true if no duplicates are found
  return true;
};