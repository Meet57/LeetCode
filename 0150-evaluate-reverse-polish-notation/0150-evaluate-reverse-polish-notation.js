/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
    let stack = [];

    for (let ele of tokens) {
        if (!["+", "-", "*", "/"].includes(ele)) {
            stack.push(parseInt(ele));
        } else {
            let right = stack.pop();
            let left = stack.pop();

            if (ele === "/") {
                stack.push(Math.trunc(left / right)); // Ensures truncation towards zero
            } else if (ele === "*") {
                stack.push(left * right);
            } else if (ele === "-") {
                stack.push(left - right);
            } else if (ele === "+") {
                stack.push(left + right);
            }
        }
    }

    return stack.pop();
};