import java.util.*;
public class Hello{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String S ="";
        for(int ctr=0; ctr<N; ctr++){
            S+=sc.nextLine(); 
            System.out.println(S);
            S = S.substring(0,ctr+1);
       }
    }
}