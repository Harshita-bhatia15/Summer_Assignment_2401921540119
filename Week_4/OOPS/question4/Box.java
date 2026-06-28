package question4;

public class Box {
    public double length;
    public double breadth;

    public Box(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    public double area() {
        return length*breadth;
    }
}

