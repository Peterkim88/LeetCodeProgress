/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // const splitStr = s.toLowerCase();
    // const lowerCased = splitStr.split('')
    let modified = [];
    let reversed = [];
    // for (let i = 0; i < lowerCased.length; i++){
    //     if ((lowerCased[i] === "a" ||
    //        lowerCased[i] === "b" ||
    //        lowerCased[i] === "c" ||
    //        lowerCased[i] === "d" ||
    //        lowerCased[i] === "e" ||
    //        lowerCased[i] === "f" ||
    //        lowerCased[i] === "g" ||
    //        lowerCased[i] === "h" ||
    //        lowerCased[i] === "i" ||
    //        lowerCased[i] === "j" ||
    //        lowerCased[i] === "k" ||
    //        lowerCased[i] === "l" ||
    //        lowerCased[i] === "m" ||
    //        lowerCased[i] === "n" ||
    //        lowerCased[i] === "o" ||
    //        lowerCased[i] === "p" ||
    //        lowerCased[i] === "q" ||
    //        lowerCased[i] === "r" ||
    //        lowerCased[i] === "s" ||
    //        lowerCased[i] === "t" ||
    //        lowerCased[i] === "u" ||
    //        lowerCased[i] === "v" ||
    //        lowerCased[i] === "w" ||
    //        lowerCased[i] === "x" ||
    //        lowerCased[i] === "y" ||
    //        lowerCased[i] === "z" ||
    //        lowerCased[i] === "0" ||
    //        lowerCased[i] === "1" ||
    //        lowerCased[i] === "2" ||
    //        lowerCased[i] === "3" ||
    //        lowerCased[i] === "4" ||
    //        lowerCased[i] === "5" ||
    //        lowerCased[i] === "6" ||
    //        lowerCased[i] === "7" ||
    //        lowerCased[i] === "8" ||
    //        lowerCased[i] === "9" )
    //        ){
    //         modified.push(lowerCased[i].toLowerCase());
    //         reversed.unshift(lowerCased[i].toLowerCase());
    //     }
    // }
    // for (let i = 0; i < modified.length; i++){
    //     if (modified[i] !== reversed[i]){
    //         return false;
    //     }
    // }
    // if (modified.length === undefined && reversed.length === undefined){
    //     return true;
    // }
    // return true;
    const alphabet = '0123456789abcdefghijklmnopqrstuvwxyz';
    const split = s.toLowerCase().split('');
    for (let i = 0; i < split.length; i++){
        if (alphabet.includes(split[i])){
            modified.push(split[i]);
            reversed.unshift(split[i]);
        }
    }
    return modified.join('') == reversed.join('')
};