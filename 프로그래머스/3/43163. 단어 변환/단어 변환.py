from collections import deque, defaultdict

def solution(begin, target, words):
    answer = 0
    
    # {"hit" : {"hot": 1, "dot": 2, ...},
    #  "hot" : {"hot": 0}, "dot": 1, ...},
    #   ... }
    words_diff = defaultdict(dict)
    
    for word1 in words:
        words_diff[begin][word1] = sum(c1 != c2 for c1, c2 in zip(begin, word1))
        for word2 in words:
            words_diff[word1][word2] = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    
    # BFS Queue
    queue = deque()
    
    # visited set
    visited = set()
    
    # It's gonna be the answer
    depth = 0
    
    queue.append((begin, depth))
    
    while(queue):
        current_word = queue.popleft()
        
        if (current_word[0] == target):
            answer = current_word[1]
            break
        
        next_words = [word for word, count in words_diff[current_word[0]].items() if word not in visited and count == 1]
        for word in next_words:
            queue.append((word, current_word[1]+1))
            visited.add(word)
    
    return answer