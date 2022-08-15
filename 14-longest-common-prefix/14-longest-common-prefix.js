/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let prefixes = {};
    strs.forEach(str => {
        let chars = str.split("");
        for (i = 0; i < chars.length; i++){
            let prefix = chars.slice(0, i+1).join("")
            if (!prefixes[prefix] && prefix.length >= 1){
                prefixes[prefix] = 1;
            } else {
                prefixes[prefix] += 1;
            }
        }
    })
    let commonPrefix = "";
    Object.entries(prefixes).forEach(([k, v]) => {
        if (v === strs.length){
            commonPrefix = k
        }   
    })
    return commonPrefix;
};