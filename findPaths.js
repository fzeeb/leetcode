/*
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
*/

/**
 * @param {number} m
 * @param {number} n
 * @param {number} maxMove
 * @param {number} startRow
 * @param {number} startColumn
 * @return {number}
 */
var findPaths = function(m, n, maxMove, startRow, startColumn) {
    const dp = new Array(m).fill(0).map(() => new Array(n).fill(0).map(() => new Array(maxMove + 1).fill(0)));
    const mod = 1e9 + 7;
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    for (let i = 1; i <= maxMove; i++) {
        for (let j = 0; j < m; j++) {
            for (let k = 0; k < n; k++) {
                for (const [dx, dy] of dirs) {
                    const x = j + dx;
                    const y = k + dy;
                    if (x < 0 || x >= m || y < 0 || y >= n) {
                        dp[j][k][i] += 1;
                    } else {
                        dp[j][k][i] = (dp[j][k][i] + dp[x][y][i - 1]) % mod;
                    }
                }
            }
        }
    }
    return dp[startRow][startColumn][maxMove];    
};

const m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0;
console.log(findPaths(m, n, maxMove, startRow, startColumn)); // 6