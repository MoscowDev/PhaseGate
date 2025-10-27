import java.util.Scanner;

public class DayOneTask{
	public static void main(String [] args){
		
	 Scanner scanner = new Scanner(System.in);
	 int questions = 10;
	 int rightAnswer = 0; 
	 long countTime = System.currentTimeMillis();

	 int count = 0;
	

	  while(count < questions){
	  int first = (int)(Math.random()*10);
	  int second = (int)(Math.random()*10);
	   count++;


	  int store = first;
	  first = second;
	  second = store;
 	 
	 System.out.printf("What is %d %s %d %s",first, " - " , second , "=");
	 int answer = scanner.nextInt();
		
	 if(first - second == answer){
	 System.out.println("You are right, good job! ");
	 rightAnswer++;
	 }

	else if(first - second != answer){
	System.out.print("You can try again: " + first + "-" +  second + ":");
	answer = scanner.nextInt();

	if(first - second == answer){
	System.out.println("correct answer. Good job! ");
	rightAnswer++;
	
	}else{
	System.out.println("wrong result!");
	System.out.printf("wrong! %n The right answer is: %d %s %d %s %d%n", first, "-", second, "=",(first - second));

        }
             	
	}
	 
	  
		 
	 }
		long stopTime = System.currentTimeMillis();
	 
	 System.out.printf("The total number of your score is %d%s%d%n ", rightAnswer, "/", questions);	
	 long sumTime = countTime - stopTime ;
	 System.out.print("The time spent in seconds " + sumTime + "seconds");
	 

 }
}
