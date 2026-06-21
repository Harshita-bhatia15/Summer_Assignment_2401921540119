import java.util.Random;
public class TestCompartment {
    public static void main(String[] args){
        Compartment[] compartment = new Compartment[10];
        Random random = new Random();

        for(int i=0; i<10; i++){
            int choice = random.nextInt(4)+1;

            switch (choice){
                case 1:
                    compartment[i] = new FirstClass();
                    break;

                case 2:
                    compartment[i] = new General();
                    break;

                case 3:
                    compartment[i] = new Ladies();
                    break;

                case 4:
                    compartment[i] = new Luggage();
                    break;
            }
        }
        System.out.println("Compartments Information");
        for (int i=0; i<10; i++){
            System.out.println("Compartment" + (i+1));
            System.out.println(compartment[i].notice());
            System.out.println();
        }

    }
}
