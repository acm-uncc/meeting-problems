/**
  Major credit to Matthew Goodman
  Typing by Nick Breaton :) 
*/

import java.util.Scanner;

public class StandingOvation {
  public static void main(String[] args) {
    Scanner k = new Scanner(System.in);
    int t = k.nextInt() + 1;
    for (int i = 1; i < t; i++) {
      int n = k.nextInt();
      String[] raw = k.next().split("");
      int[] people = new int[n + 1];
      for (n = n; n >= 0; n--) {
         people[n] = Integer.parseInt(raw[n]);
      }
      int standing = people[0];
      int friends = 0;
      for (n = 1; n < people.length; n++) {
         if (people[n] > 0) {
            if (standing < n) {
               friends += n - standing;
               standing = n;
            }
            standing += people[n];   
         }
      }
      System.out.println("Case #" + (i) + ": " + friends);
    }
  }
}
