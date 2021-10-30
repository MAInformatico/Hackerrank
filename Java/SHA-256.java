import java.util.Scanner;
import java.security.MessageDigest;

public class Solution {

    public static void main(String[] args) throws java.security.NoSuchAlgorithmException{
        System.out.println(javax.xml.bind.DatatypeConverter.printHexBinary(MessageDigest.getInstance("SHA-256").digest(new Scanner(System.in).nextLine().getBytes())).toLowerCase());
    }
}
