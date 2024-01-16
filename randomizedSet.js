
var RandomizedSet = function() {
    this.set = new Set();
    this.arr = [];  
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if (!this.set.has(val)) {
      this.set.add(val);
      this.arr.push(val);
      return true;
    }
    return false;
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if (this.set.has(val)) {
      this.set.delete(val);
      this.arr.splice(this.arr.indexOf(val), 1);
      return true;
    }
    return false;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    return this.arr[Math.floor(Math.random() * this.arr.length)];
};

/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */

let randomizedSet = new RandomizedSet();
console.log(randomizedSet.remove(2)); // Returns false as 2 does not exist in the set.
console.log(randomizedSet.insert(1)); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
console.log(randomizedSet.insert(2)); // Inserts 2 to the set, returns true. Set now contains [1,2].
console.log(randomizedSet.getRandom()); // getRandom() should return either 1 or 2 randomly.
console.log(randomizedSet.remove(1)); // Removes 1 from the set, returns true. Set now contains [2].
console.log(randomizedSet.insert(2)); // 2 was already in the set, so return false.
console.log(randomizedSet.getRandom()); // Since 2 is the only number in the set, getRandom() will always return 2.