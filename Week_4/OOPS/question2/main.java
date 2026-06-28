package question2;

public class main {
    public static void main(String[] args) {

        Outer outer = new Outer();

        outer.display();

        Outer.Inner inner = outer.new Inner();

        inner.display();

    }
}
