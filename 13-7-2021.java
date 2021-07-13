import java.util.*;

class Company{
    private String domainName;
    public Company(String domainName){
        this.domainName = domainName;
    }
    public String generateEmailId(String name, String designation){
        return String.format("%s.%s@%s",name,designation,this.domainName).toLowerCase();
    }
}

public class Hello{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String domainName = sc.nextLine().trim();
        Company company = new Company(domainName);
        int N = Ingeger.parseINt(sc.nextLine().trim());
        for(int ctr = 1; ctr <= N; ctr++){
            String emp[] = sc.nextLine().trim().split("\\s+");
            System.out.println(company.generateEmailId(emp[0],emp[1]));
        }
    }
}