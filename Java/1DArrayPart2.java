import java.util.*;

public class Solution {

    public static boolean canWin(int leap, int[] game) {
        int i=0,ptr=0;
        int size=game.length;
        boolean result=false;        
          while(i<size){
            if(i+leap<=size-1 && game[i+leap]==0 && leap!=0) i=i+leap;
            else if(i+1<=size-1 && game[i+1]==0) i=i+1;
            else if(i-1>=0 && game[i-1]==0) i=i-1;
            else return result;
            game[i]=1;
            if(i==size-1 || i+leap>=size) result=true;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
