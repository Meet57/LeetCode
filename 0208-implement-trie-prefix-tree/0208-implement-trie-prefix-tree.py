class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

# Operations
# Insert (insert(word))

# Traverse the Trie, creating nodes if necessary.
# Mark the last node as the end of a word.
# Search (search(word))

# Traverse the Trie to check if the word exists.
# Return True only if it's a complete word (isEnd = True).
# Prefix Check (startsWith(prefix))

# Similar to search(), but only verifies if the prefix exists.

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True   


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)