
	 let questions = 10;
	 let rightAnswer = 0; 
	 let countTime = System.currentTimeMillis();

	 let count = 0;
	

	  while(count < questions){
	  let first = (let)(Math.random()*10);
	  let second = (let)(Math.random()*10);
	   count++;


	  let store = first;
	  first = second;
	  second = store;

 	let prompt = require('prompt-sync')()
	console.log  prompt(input(first , second));
	 
		
	 if(first - second == answer){
	 console.log("You are right, good job! ");
	 rightAnswer++;
	 

	else if(first - second != answer)
	console.log prompt(input("You can try again: " + first + "-" +  second + ":"));
	

	if(first - second == answer){
	console.log("correct answer. Good job! ");
	rightAnswer++;
	
	}else{
	console.log("wrong result!");
	console.log("wrong! %n The right answer is: %d %s %d %s %d%n", first, "-", second, "=",(first - second));

        

	let stopTime = System.currentTimeMillis();
	 
	 console.log("The total number of your score is %d%s%d%n ", rightAnswer, "/", questions);	
	 let sumTime = countTime - stopTime ;
	 console.log("The time spent in seconds " + sumTime + "seconds");
	 


