
let multiple = 1;
let sum = 0;
let sumtwo = 0;
let square = 0;

for(let count = 1; count<=10; count++){
	if(count % 4 == 0){

		
		multiple = 1;
		sum = 0;
	

		for (let counter = 1; counter <= 5; counter ++){
			multiple = multiple * count;
			sum = sum + multiple;
			
			

		
}
sumtwo = sum + sumtwo;
square = sumtwo * sumtwo;
	}

}
console.log (square);