import java.text.DecimalFormat;
import java.util.*;

class Person{
    private String name;
    private  int weight;
    private  double height;
    Person(String name,int weight,double height){
        this.name = name;
        this.weight = weight;
        this.height = height;
    }
    public double getBodyMassIndex(){
        return weight/(height*height);
    }
    
    @Override
    public String toString(){
        String precisize = String.format("%.2f",height);
        return "Name: "+name+"\n"+"Weight: "+weight+" kg"+"\n"+"Height: "+precisize+" m";
    }
}

public class Hello {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        String name = sc.nextLine().trim();
        int weight = sc.nextInt();
        double height = sc.nextDouble();
        Person person = new Person(name, weight, height);
        System.out.println(person);
        System.out.printf("BMI: %.1f", person.getBodyMassIndex());
    }
}