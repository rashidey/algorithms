'''
Given two words (beginWord and endWord), and a dictionary's word list, find all 
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a 
transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible 
transformation.
'''

from collections import defaultdict, deque
import string
def generateNeighbors(word, wordList):
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            candidate = word[:i] + letter + word[i+1:]
            if candidate in wordList:
                yield candidate
def createAllPaths(parentDict, word, beginWord):
    if word == beginWord:
        return [[beginWord]]
    output = []
    for w in parentDict[word]:
       x = createAllPaths(parentDict, w, beginWord)
       for l in x:
           l.append(word)
           output.append(l)
    return output

def word_ladder_v2(beginWord, endWord, wordList):
    q = deque([beginWord ])
    seen = set([beginWord])
    wordList = set(wordList)
    parents = defaultdict(set)
    while q:
        num_in_level = len(q)
        finished = False
        seen_this_level = set()
        for i in range(num_in_level):
            q_item = q.popleft()
            for candidate in generateNeighbors(q_item, wordList):
                if candidate == endWord:
                    finished = True
                elif candidate in seen:
                    continue
                if candidate not in seen_this_level:
                    q.append(candidate)
                seen_this_level.add(candidate)
                parents[candidate].add(q_item)
        if finished:
            break
        seen |= seen_this_level
    return createAllPaths(parents, endWord, beginWord)


#print(word_ladder_v2('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
#print(word_ladder_v2('a', 'c', ['a', 'b', 'c']))

import string

def word_ladder_v3(first, last, words):
	graph = defaultdict(list)
	words.append(first)
	words = set(words)

	for word in words:
		for i in range(len(word)):
			for letter in string.ascii_lowercase:
				candidate = word[:i] + letter + word[i+1:]
				if candidate in words and candidate != word:
					graph[word].append(candidate)

	#print(graph)

	visited, path, result = set(), list(), set()
	'''
	generate_paths(first, last, visited, path, result, graph)
	minx = float('inf')
	for val in result:
		if len(val) < minx:
			minx = len(val)
	final = []
	for val in result:
		if len(val) == minx:
			final.append(val)
	return final
	'''
	
	distances = {}
	parents = defaultdict(list)
	


def generate_paths(first, last, visited, path, result, graph):
	visited.add(first)
	path.append(first)
	#print(graph, first, last)
	if first == last:
		#print(result)
		result.add(tuple(path[:]))
	else:
		for vertex in graph[first]:
			if vertex not in visited:
				generate_paths(vertex, last, visited, path, result, graph)

	path.pop()
	visited.remove(first)

def bfs(root, graph):
		que = deque([root])
		visited = set()
		result = []
		parents = {}
		parents[root] = -1

		while len(que) > 0:
			current = que.popleft()
			visited.add(current)
			result.append(current)

			for vertex in graph[current]:
				if vertex not in visited:
					parents[vertex] = current
					visited.add(vertex)
					que.append(vertex)

		return result

#print(word_ladder_v3('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
#print(word_ladder_v3('a', 'c', ['a', 'b', 'c']))

s = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
print(word_ladder_v3('kid', 'luz', s))
