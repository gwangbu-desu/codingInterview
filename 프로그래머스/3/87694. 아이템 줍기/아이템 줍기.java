import java.util.*;
class Solution {
    class Rectangle{
        int x1; // 좌측 하단
        int y1; // 좌측 하단
        int x2; // 우측 상단
        int y2; // 우측 상단
        public Rectangle(int x1,int y1,int x2,int y2){
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
        }
        @Override
        public String toString(){
            return String.format("(%d,%d) (%d,%d)\n",x1,y1,x2,y2);
        }
        // 테두리임
        public boolean isLine(int x, int y){
            if(isIn(x,y) && (x1 == x || x2 == x || y1 == y || y2 ==y)){
                // System.out.printf("%s -> (%d, %d)\n",this.toString(),x,y);
                
                System.out.printf("(%d, %d)\n",x,y);
                return true;
            }
            return false;
        }
        
        // 사각형 내부에 있음 (테두리가 아님)
        public boolean isIn(int x, int y){
            if( x1 < x && y1 < y && x < x2 && y < y2){
                return true;
            }
            return false;
        }
    }
    public static final List<Rectangle> recList = new ArrayList<>();
    public static final int[] dx = {0,1,0,-1};
    public static final int[] dy = {1,0,-1,0};
    public static boolean[][] arr = new boolean[103][103];
    public static boolean[][] visited = new boolean[103][103];
    public static int goalX;
    public static int goalY;
    public static int answer;
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        answer = Integer.MAX_VALUE;
        goalX = itemX*2;
        goalY = itemY*2;
        // 좌표 확장 -> 모든 값 2배로 늘리기. [TODO]answer는 절반으로 반환해야됨.
        for(int[] rec : rectangle){
            for(int x=rec[0]*2;x<=rec[2]*2;x++){
                for(int y = rec[1]*2; y<=rec[3]*2; y++){
                    arr[y][x] = true;
                }
            }
        }
        for(int[] rec : rectangle){
            for(int x=rec[0]*2+1;x<rec[2]*2;x++){
                for(int y = rec[1]*2+1; y<rec[3]*2; y++){
                    arr[y][x] = false;
                }
            }
        }
        
        visited[characterY*2][characterX*2]= true;
        dfs(characterX*2,characterY*2,0);
        return answer / 2;
    }
    
    public void dfs(int x, int y, int distance){
        if( x== goalX && y==goalY){
            answer = Math.min(answer, distance);
            System.out.println(distance);
            visited[y][x]=false;
            return;
        }
        // 4방향 탐색
        int nx;
        int ny;
        for(int dir = 0;dir<4;dir++){
            nx = x + dx[dir];
            ny = y + dy[dir];
            
            if(!check(nx,ny)) continue;
            // System.out.println(1);
            
            // 이미 방문함
            if(visited[ny][nx]) {
                visited[ny][nx] = true;
                continue;
            }
            visited[ny][nx] = true;
            // System.out.println(2);
            
            // 테두리 or 사각형 내부가 아님
            if(!arr[ny][nx]) continue;
            // System.out.println(3);
            // System.out.printf("(%d,%d)\n",nx,ny);
            dfs(nx,ny, distance+1);
        }
    }
    
    public boolean check(int x, int y){
        if ( x < 0 || 102 < x || y < 0 || 102 < y ) return false;
        return true;
    }
}