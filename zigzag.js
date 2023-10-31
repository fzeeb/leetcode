/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {

  // if numRows is 1, return s
  if (numRows === 1) {
    return s;
  } 

  // create an array of strings, each string is a row
  let rows = [];
  for (let i = 0; i < numRows; i++) {
    rows.push('');
  }

  // iterate through s
  // if going down, add to row
  // if going up, add to row
  // if at top, go down
  // if at bottom, go up
  let goingDown = true;
  let currentRow = 0;
  for (let i = 0; i < s.length; i++) {
    rows[currentRow] += s[i];
    if (goingDown) {
      currentRow++;
    } else {
      currentRow--;
    }
    if (currentRow === numRows - 1) {
      goingDown = false;
    } else if (currentRow === 0) {
      goingDown = true;
    }
  }

  // join the rows
  return rows.join('');
};