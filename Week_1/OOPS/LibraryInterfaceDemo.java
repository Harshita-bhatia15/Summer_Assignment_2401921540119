public class LibraryInterfaceDemo {
    public static void main(String[] args){
        KidUsers k1 = new KidUsers(10, "kids");
        k1.registerAccount();
        k1.requestBook();

        KidUsers k2 = new KidUsers(18, "Fiction");
        k2.registerAccount();
        k2.requestBook();

        AdultUser A1 = new AdultUser(5, "kids");
        A1.registerAccount();
        A1.requestBook();

        AdultUser A2 = new AdultUser(23, "Fiction");
        A2.registerAccount();
        A2.requestBook();

    }
}
