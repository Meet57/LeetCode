/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    m = {}
    count = 0

    for(let i=0; i<s.length; i++) {
        m[s[i]] = (m[s[i]] || 0) + 1

        if(m[s[i]]%2 == 0) {
            count += 2
        }
    }

    if(count < s.length){
        count += 1
    }

    return count
};