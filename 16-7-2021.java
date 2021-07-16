import java.util.*;

class City implements Comparable<City>
{
    private String name;
    private int menCount,womenCount;
    public City(String name, int menCount, int womenCount)
    {
        this.name = name;
        this.menCount = menCount;
        this.womenCount = womenCount;
    }

    @Override 
    public String toString()
    {
        return String.format("%s %d %d",this.name,this.menCount,this.womenCount);

    }

    @Override 
    public int compareTo(City other)
    {
        if(this.menCount+this.womenCount == other.menCount+other.womenCount)
        {
            if(this.menCount == other.menCount)
            {
                return this.name.compareTo(other.name);
                
            }
            return other.menCount-this.menCount;
        }
        return (other.menCount+other.womenCount) - (this.menCount+this.womenCount);
    }
}


public class Hello{
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine().trim());
        List<City> cities = new ArrayList<>();
        for (int ctr=1; ctr <=N; ctr++){
            String currCity[] = sc.nextLine().trim().split("\\s+");
            cities.add(new City(currCity[0]),
            Integer.parseInt(currCity[1]),
            Integer.parseInt(cur[2]));
        }
        Collections.sort(cities);
        for (City city : cities) {
            System.out.println(city);
        }
    }
}