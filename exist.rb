=begin
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
=end
# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
class TrieNode
  attr_accessor :children, :word

  def initialize
    @children = {}
    @word = nil
  end
end

def exist(board, word)
  root = build_trie(word)
  board.each_with_index do |row, i|
    row.each_with_index do |cell, j|
      return true if dfs(board, i, j, root)
    end
  end
  false
end

def dfs(board, i, j, node)
  return false if i < 0 || i >= board.length || j < 0 || j >= board[0].length || !node.children[board[i][j]]
  return true if node.children[board[i][j]].word

  temp = board[i][j]
  board[i][j] = '#'
  node = node.children[temp]

  found = dfs(board, i - 1, j, node) ||
          dfs(board, i + 1, j, node) ||
          dfs(board, i, j - 1, node) ||
          dfs(board, i, j + 1, node)

  board[i][j] = temp
  node.word = nil if found
  found
end

def build_trie(word)
  root = TrieNode.new
  node = root
  word.each_char do |char|
    node.children[char] ||= TrieNode.new
    node = node.children[char]
  end
  node.word = word
  root
end

board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAABAA"
puts exist(board, word) # false

=begin
Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
=end