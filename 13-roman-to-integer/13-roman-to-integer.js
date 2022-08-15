/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    
    const values = {
        I:1,
        V:5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000
    }
    
    const chars = s.split("");
    
    let num = 0
    
    for (let i = 0; i < chars.length; i++){
        if (chars[i] === "I" && chars[i+1] === "V"){
            num += 4;
            i++;
        } else if (chars[i] === "I" && chars[i+1] === "X"){
            num += 9;
            i++;
        } else if (chars[i] === "X" && chars[i+1] === "L"){
            num += 40;
            i++;   
        } else if (chars[i] === "X" && chars[i+1] === "C"){
            num += 90;
            i++;   
        } else if (chars[i] === "C" && chars[i+1] === "D"){
            num += 400;
            i++;  
        } else if (chars[i] === "C" && chars[i+1] === "M"){
            num += 900;
            i++;    
        } else {
            num += values[chars[i]]
        }
    }
    
    return num;
    
};