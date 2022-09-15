import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		String line = new Scanner(System.in).nextLine();

		int[] digits  = new int[4];

		for (int i = 0; i < 4; i++) {
			digits[i] = line.charAt(i) - '0';
		}

		for (int y = 3; y >= 0; y--) {
			for (int x = 0; x < 4; x++) {
				if (((digits[x] >> y) & 1) == 0) {
					System.out.print(".");
				} else {
					System.out.print("*");
				}

				if (x == 1) {
					System.out.print("  ");
				} else if (x < 3) {
					System.out.print(" ");
				}

			}

			System.out.println();
		}
	}
}
