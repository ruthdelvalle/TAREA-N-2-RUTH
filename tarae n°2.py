import java.util.Scanner;

public class EvaluacionTemperaturaTanque {

    public static void main(String[] args) {
        // Definición de parámetros predeterminados
        int[][] valoresPredeterminados = {
                // Mañana, Tarde, Noche
                {10, 15, 12}, // Muy Buena
                {20, 25, 22}, // Normal
                {30, 35, 32}  // Peligrosa
        };

        Scanner scanner = new Scanner(System.in);

        // Solicitud de datos al usuario
        System.out.println("Ingrese el momento del día (mañana, tarde, noche):");
        String momentoDia = scanner.nextLine().toLowerCase();
        System.out.println("Ingrese la temperatura actual del tanque de combustible:");
        double temperatura = scanner.nextDouble();

        // Evaluación de la temperatura
        int indiceMomentoDia = obtenerIndiceMomentoDia(momentoDia);
        if (indiceMomentoDia == -1) {
            System.out.println("Error: Momento del día no válido");
            return;
        }

        String resultadoEvaluacion = evaluarTemperatura(valoresPredeterminados, indiceMomentoDia, temperatura);

        // Resultado de la evaluación
        System.out.println("La temperatura del tanque de combustible es: " + resultadoEvaluacion + " para el " + momentoDia);
    }

    public static int obtenerIndiceMomentoDia(String momentoDia) {
        switch (momentoDia) {
            case "mañana":
                return 0;
            case "tarde":
                return 1;
            case "noche":
                return 2;
            default:
                return -1; // Valor por defecto si el momento del día no es válido
        }
    }

    public static String evaluarTemperatura(int[][] valoresPredeterminados, int indiceMomentoDia, double temperatura) {
        int[] valores = valoresPredeterminados[indiceMomentoDia];

        if (temperatura < valores[0]) {
            return "Muy Buena";
        } else if (temperatura <= valores[1]) {
            return "Normal";
        } else {
            return "Peligrosa";
        }
    }
}

