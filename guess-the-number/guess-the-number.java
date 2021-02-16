import java.util.Random;
import java.util.Scanner;
import java.lang.System;

public class Game {

    public static void main(String[] args){



        System.out.println("Hello and welcome to my number guessing game.");
        System.out.println("Pick a number: ");

        Scanner inputnum = new Scanner(System.in); 
        maxnum = inputnum.nextInt();

        Random rand = new Random();
        int number = rand.nextInt(maxnum);
        int tries = 0;
        Scanner input = new Scanner(System.in);
        int guess;
        boolean win = false;

        while (win == false){ 

            System.out.println("Guess a number between 1 and "+ maxnum +": ");
            guess = input.nextInt();
            tries++; 

            if (guess == number){
                win = true; 
            }

            else if(guess < number){
                System.out.println("Number is to low, tray again");
            }

            else if(guess > number){
                System.out.println("Number is to high, try again");
            }

        }

        System.out.println("You win!");
        System.out.println("It took you "+ tries + " tries.");

    }
}
