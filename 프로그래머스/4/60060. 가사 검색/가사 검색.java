import java.util.*;
    class TrieNode{
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isEnd;
        int count;
    }
    
    class Trie{
        private final TrieNode root = new TrieNode();
        public void insert(String word){
            TrieNode node = root;
            node.count++;
            for(char c: word.toCharArray()){
                node.children.putIfAbsent(c, new TrieNode());
                node = node.children.get(c);
                node.count++;
            }
            
            node.isEnd = true;
        }
        
        public boolean search(String word){
            TrieNode node = root;
            
            for(char c:word.toCharArray()){
                node = node.children.get(c);
                if(node == null) return false;
            }
            
            return node.isEnd;
        }
        
        public boolean startsWith(String prefix){
            TrieNode node = root;
            for(char c: prefix.toCharArray()){
                node = node.children.get(c);
                if(node == null) return false;
            }
            
            return true;
        }
        
        public int find(String prefix){
            TrieNode node = root;
            for(char c:prefix.toCharArray()){
                node = node.children.get(c);
                if(node == null) return 0;
            }
            return node.count;
        }
    }
class Solution {
    
    
    public int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];
        Map<Integer, Trie> trieMap = new HashMap<>();
        Map<Integer, Trie> reverseMap = new HashMap<>();
        StringBuilder sb;
        // Trie 사용하기.
        for(String word: words){    
            int len = word.length();
            trieMap.putIfAbsent(len, new Trie());
            reverseMap.putIfAbsent(len, new Trie());
            sb = new StringBuilder();
            sb.append(word);
            trieMap.get(len).insert(word);
            reverseMap.get(len).insert(sb.reverse().toString());
        }
        for(int i=0; i<queries.length;i++){
            String query = queries[i];
            int len = query.length();
            if(!trieMap.containsKey(len)) {
                answer[i] = 0;
                continue;
            }
            if (query.charAt(0) == '?'){
                sb = new StringBuilder();
                sb.append(query);
                query = sb.reverse().toString().replace("?","");
                answer[i] = reverseMap.get(len).find(query);
            }else{
                query = query.replace("?","");
                // System.out.println(query);
                answer[i] = trieMap.get(len).find(query);   
            }
        }
        return answer;
    }
}