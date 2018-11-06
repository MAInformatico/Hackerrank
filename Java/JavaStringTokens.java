import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      String s=sc.nextLine();
      s.trim();
      StringTokenizer parts = new StringTokenizer(s,("[_\\@!?.', ]"));
        int x = parts.countTokens();
        System.out.println(x);
        while(parts.hasMoreTokens()){
            System.out.println(parts.nextToken());
        }
     scan.close(); 
    }
}
