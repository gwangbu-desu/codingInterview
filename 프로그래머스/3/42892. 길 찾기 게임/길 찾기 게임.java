import java.util.*;
class Solution {
    class Node{
        int x, y, idx;
        Node left;
        Node right;
        Node (int x, int y, int idx){
            this.x = x;
            this.y = y;
            this.idx = idx;
        }
        void update(Node child){
            if(child.x > this.x){
                if(this.right == null){
                    // 오른쪽 노드에 넣기.
                    this.right = child;
                }else{
                    this.right.update(child);
                }
            }else if(child.x < this.x){
                if(this.left == null){
                    // 왼쪽 노드에 넣기.
                    this.left = child;
                }else{
                    this.left.update(child);
                }
            }
        }
        @Override
        public String toString(){
            return String.format("%d %d %d",this.x,this.y,this.idx);
        }
    }
    ArrayList<Node> nodes = new ArrayList<>();
    public int count = 0;
    int[][] answer = new int[2][];
    public int[][] solution(int[][] nodeinfo) {
        
        answer[0] = new int[nodeinfo.length];
        answer[1] = new int[nodeinfo.length];
        
        // init
        for(int idx=0;idx<nodeinfo.length;idx++){
            // 1-index이니 idx+1 로 저장.
            nodes.add(new Node(nodeinfo[idx][0],nodeinfo[idx][1],idx+1));
        }
        // y값 기준으로 정렬 (내림차순)
        Collections.sort(nodes,(a,b)-> b.y - a.y);
        // for(Node a : nodes){
        //     System.out.println(a);
        // }
        Node root = nodes.get(0);
        
        for(int i=1;i<nodeinfo.length;i++){
            // root 기준으로 트리 업데이트
            root.update(nodes.get(i));
        }
        // 전위
        pre(root);
        // 후위
        count = 0;
        // System.out.println();
        post(root);
        return answer;
    }
    public void pre(Node cur){
        answer[0][count++] = cur.idx;
        // System.out.println(cur);
        if(cur.left != null) pre(cur.left);
        if(cur.right != null) pre(cur.right);
    }
    public void post(Node cur){
        if(cur.left != null) post(cur.left);
        if(cur.right != null) post(cur.right);
        answer[1][count++] = cur.idx;
    }
}