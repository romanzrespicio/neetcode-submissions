class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self, word, i):
        curr = self
        curr.refs += 1

        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.refs += 1
        curr.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def getIndex(c):
            index = ord(c) - ord('a')
            return index

        def dfs(r, c, node):
            # Out of bounds, cell already used in curr path, or trie has no child for board[r][c]
            if (r < 0 or c < 0 or r>= ROWS or c >= COLS
            or board[r][c] == "*" or 
            not node.children[getIndex(board[r][c])]):
                return 0
            
            tmp = board[r][c] # get character
            board[r][c] = "*" # mark visited
            prev = node
            node = node.children[getIndex(tmp)]
            found = 0

            if node.idx != -1: # end of word found
                res.append(words[node.idx])
                node.idx = -1
                found += 1
            
            # Recursively check in all direction of matrix
            found += dfs(r + 1, c, node)
            found += dfs(r - 1, c, node)
            found += dfs(r, c + 1, node)
            found += dfs(r, c - 1, node)

            board[r][c] = tmp # restore to original value
            node.refs -= found # decrement references if no more words go down this path.
            if not node.refs: # if no more references, prune
                prev.children[getIndex(tmp)] = None

            return found

        for r in range(ROWS):
            for c in range(COLS):
                root.refs -= dfs(r, c, root)
        
        return res
        

        