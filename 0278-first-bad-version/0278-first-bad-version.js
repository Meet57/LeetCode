/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function (isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function (n) {
        var first = 1
        var last = n

        while (first < last) {
            var mid = Math.floor((first + last) / 2)

            if (isBadVersion(mid)) {
                last = mid
            } else {
                first = mid + 1
            }
        }

        return first
    };
};