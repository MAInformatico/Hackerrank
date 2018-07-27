import java.util.*;

public class Solution {

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int d = scan.nextInt();
        int[] data = new int[n];
        for(int i=0; i<n;i++)  data[(i+n-d)%n] = scan.nextInt();
        
        for(int i=0; i<n;i++)  System.out.print(data[i] + " ");
        
    }
}
