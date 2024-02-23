/*
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
*/
/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    const graph = {};
    for (const [from, to, price] of flights) {
        if (!graph[from]) graph[from] = [];
        graph[from].push([to, price]);
    }
    const queue = [[src, 0, 0]];
    while (queue.length) {
        const [city, stops, cost] = queue.shift();
        if (city === dst) return cost;
        if (stops > k) continue;
        if (graph[city]) {
            for (const [next, price] of graph[city]) {
                queue.push([next, stops + 1, cost + price]);
            }
        }
        queue.sort((a, b) => a[2] - b[2]);
    }
    return -1;
};

const n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
console.log(findCheapestPrice(n, flights, src, dst, k)); // 700