import java.util.*;

class Person{
    private String name;
    private int age;
    public Person(){
        this.name="person";
        this.age=0;
    }
    
    public Person(String name){
        this.name = name;
        this.age = 0;
    }

    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString(){
        return this.name+":"+this.age;
    }
}

public class Hello{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int query = Integer.parseInt(sc.nextLine().trim());
        Person p = null;
        if (query == 1){
            p = new Person();
        }else if (query == 2){
            String name = sc.nextLine();
            p = new Person(name);
        }else if (query == 3){
            String name = sc.nextLine();
            int age = Integer.parseInt(sc.nextLine().trim());
            p = new Person(name, age);
        }
        System.out.println(p);
    } //end of main method
} // end of Hello class