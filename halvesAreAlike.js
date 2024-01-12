/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    let a = s.slice(0, s.length/2);
    let b = s.slice(s.length/2, s.length);

    let countA = 0;
    let countB = 0;

    for (let i = 0; i < a.length; i++) {
        if (a[i].match(/[aeiouAEIOU]/g)) {
            countA++;
        }
    }
    for (let i = 0; i < b.length; i++) {
        if (b[i].match(/[aeiouAEIOU]/g)) {
            countB++;
        }
    }
    return countA === countB;
};

const s = "book";
console.log(halvesAreAlike(s)); // true