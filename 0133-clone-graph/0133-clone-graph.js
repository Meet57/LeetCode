/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

const clone = (node, clones = {}) => {
    if(!node){
        return null
    }

    if(clones[node.val]){
        return clones[node.val]
    }

    const cloneNode = new _Node(node.val)
    clones[node.val] = cloneNode

    for (let neighbor of node.neighbors) {
        cloneNode.neighbors.push(clone(neighbor, clones))
    }

    return cloneNode
}

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    return clone(node)
};