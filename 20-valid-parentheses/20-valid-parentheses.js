/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let steps = {};
    let currentStep = 0;
    let chars = s.split("");
    for(let i = 0; i < chars.length; i++){
        if (chars[i] === "(" || chars[i] === "[" || chars[i] === "{"){
            steps[currentStep] = chars[i];
            currentStep++;
        } else if (chars[i] === ")" && steps[currentStep-1] === "("){
            currentStep--;
            steps[currentStep] = null;
        } else if (chars[i] === "]" && steps[currentStep-1] === "["){
            currentStep--;
            steps[currentStep] = null;
        } else if (chars[i] === "}" && steps[currentStep-1] === "{"){
            currentStep--;
            steps[currentStep] = null;
        } else {
            return false
        }
    }
    return Object.values(steps).every(value => value === null)
};