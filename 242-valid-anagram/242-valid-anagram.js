/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let hash = {};
    let sArray = s.split("");
    let tArray = t.split("");
    
    if (sArray.length !== tArray.length){
        return false;
    }
    
    for (let i = 0; i < sArray.length; i++){
        if (!hash[sArray[i]]){
            hash[sArray[i]] = 1;
        } else {
            hash[sArray[i]] += 1;
        }
    }
    for (let i = 0; i < tArray.length; i++){
        if (!hash[tArray[i]]){
            hash[tArray[i]] = -1
        } else {
            hash[tArray[i]] -= 1;
        }
    }
    for (let ch in hash){
        if (hash[ch] !== 0){
            return false;
        }
    }
    return true;
};