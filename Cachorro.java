// Class Cachorro
public class Cachorro extends Animal {
    public Cachorro(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}