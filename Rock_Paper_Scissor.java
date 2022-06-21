import java.util.Random;
import java.util.Scanner;

public class Rock_Paper_Scissor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter input '0' for Rock, '1' for Paper and '2' for Scissor");
        int userinput = sc.nextInt();

        // 0 = ROCK & 1 = PAPER & 2 = SCISSOR
        
        Random random = new Random();
        int compinput = random.nextInt(3);

        if(userinput<0||userinput>2)
            System.out.println("Invalid Input");
        else
        {
            if(userinput==compinput)
            {
                System.out.println("You chose "+userinput+"\nComputer chose "+compinput+"\nIt's a tie");
            }
            else if(userinput==0 && compinput==2 || userinput==1 && compinput==0 || userinput==2 && compinput==1)
            {
                System.out.println("You chose "+userinput+"\nComputer chose "+compinput+"\nCongrats! You win");
            } 
            else
            {
                System.out.println("You chose "+userinput+"\nComputer chose "+compinput+"\nAlas! You Lose");
            }
        }
    }
}
//CODE IS WRITTEN BY SHIRSHENDU CHATTERJEE