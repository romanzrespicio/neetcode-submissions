class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.refs = 0

    def addWord(self, word, i):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs += 1
        curr.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            # Out of bounds, or no trie child for this cell ("*" is never a key, so visited cells fail here too)
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                    or board[r][c] not in node.children):
                return 0

            tmp = board[r][c]
            board[r][c] = "*"  # mark visited
            prev = node
            node = node.children[tmp]
            found = 0

            if node.idx != -1:  # end of word found
                res.append(words[node.idx])
                node.idx = -1
                found += 1

            found += dfs(r + 1, c, node)
            found += dfs(r - 1, c, node)
            found += dfs(r, c + 1, node)
            found += dfs(r, c - 1, node)

            board[r][c] = tmp  # backtrack
            node.refs -= found
            if not node.refs:  # no unfound words left down this path, prune
                prev.children.pop(tmp)

            return found

        for r in range(ROWS):
            for c in range(COLS):
                root.refs -= dfs(r, c, root)
                if root.refs == 0:
                    return res

        return res