import java.io.*;
import java.math.*;
import java.security.*;
import java.util.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
      BigInteger n = in.nextBigInteger();
      in.close();
      System.out.println(n.isProbablePrime(1) ? "prime" :"not prime");
        
    }
}
