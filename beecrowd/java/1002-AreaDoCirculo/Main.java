import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        double raio = scanner.nextDouble();
        double quadrado_raio = Math.pow(raio, 2);
        double area = 3.14159 * quadrado_raio;
        System.out.printf("A=%.4f\n", area);
        scanner.close();
    }
}
