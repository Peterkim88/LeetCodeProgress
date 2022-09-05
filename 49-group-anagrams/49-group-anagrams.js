/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let grouping = {};
    strs.forEach(str => {
        sorted = str.split("").sort().join("");
        if (grouping[sorted] == undefined){
            grouping[sorted] = [];
        }
        grouping[sorted].push(str);
    })
    return Object.values(grouping);
};