

function isPerfectSquare(num) {
    if (num < 0) return false;
    for (let count = 0; count * count <= num; count++) {
        if (count * count === num) {
            return true;
        }
    }
    return false;
}

console.log(isPerfectSquare(16))
console.log(isPerfectSquare(3))