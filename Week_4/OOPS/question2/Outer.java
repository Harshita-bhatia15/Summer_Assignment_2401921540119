package question2;

public class Outer {
    public void display() {
        System.out.println("This is outer class");
    }

    public class Inner {

        public void display() {
            System.out.println("This is inner class");
        }

    }
}
