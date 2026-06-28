package question4;

public class Box3D extends Box{
    public double height;

    public Box3D(double length, double breadth, double height) {
        super(length, breadth);
        this.height = height;
    }

    public double volume() {
        return length*breadth*height;
    }
}
