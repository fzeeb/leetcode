/**
 * Given an m x n grid of characters board and a string word, return true if word exists in the grid.
 * The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
 * The same letter cell may not be used more than once.
 *
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
class TrieNode {
  constructor() {
    this.children = {};
    this.word = null;
  }
}

function exist(board, word) {
  const root = buildTrie(word);
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (dfs(board, i, j, root)) {
        return true;
      }
    }
  }
  return false;
}

function dfs(board, i, j, node) {
  if (
    i < 0 ||
    i >= board.length ||
    j < 0 ||
    j >= board[0].length ||
    !node.children[board[i][j]]
  ) {
    return false;
  }
  if (node.children[board[i][j]].word) {
    return true;
  }

  const temp = board[i][j];
  board[i][j] = "#";
  node = node.children[temp];

  const found =
    dfs(board, i - 1, j, node) ||
    dfs(board, i + 1, j, node) ||
    dfs(board, i, j - 1, node) ||
    dfs(board, i, j + 1, node);

  board[i][j] = temp;
  if (found) {
    node.word = null;
  }
  return found;
}

function buildTrie(word) {
  const root = new TrieNode();
  let node = root;
  for (let char of word) {
    if (!node.children[char]) {
      node.children[char] = new TrieNode();
    }
    node = node.children[char];
  }
  node.word = word;
  return root;
}

const board = [
  ["A", "A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A", "A"],
  ["A", "A", "A", "A", "A", "A"],
];
const word = "AAAAAAAAAAAABAA";
console.log(exist(board, word)); // false

/**
 * Constraints:
 * - m == board.length
 * - n = board[i].length
 * - 1 <= m, n <= 6
 * - 1 <= word.length <= 15
 * - board and word consists of only lowercase and uppercase English letters.
 */