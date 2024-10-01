public class Vetores {
    public static void main(String[] args) {
        int[] numeros = new int[3];

        // Armazenamento dos valores nas posições
        numeros[0] = 15;
        numeros[1] = 20;
        numeros[2] = 50;

        // Obter
        int num = numeros[0];
        // System.out.println(num);
        // System.out.println(numeros[1]);
        // System.out.println(numeros[2]);

        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Posição: " + i);
            System.out.println("Valor: " + numeros[i]);
            System.out.println();
        }
    }
}