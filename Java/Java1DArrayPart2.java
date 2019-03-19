import java.util.*;

public class Solution {
static int visited[];

public static boolean canWin(int[] game,int leap,int i) {
    boolean result=true;
    if(i>=game.length)
               return result;

    if(visited[i]==0){
        visited[i]=1;
        if(game[i]==0){
           if( canWin(game,leap,i+leap))
               return result;
           if( canWin(game,leap,i+1)){
               return result;
           }
            if(i!=0)
                if(canWin(game,leap,i-1))
                     return result;
        }
    }
    result=false;
    return result;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            visited=new int[n];
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(game,leap,0)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
