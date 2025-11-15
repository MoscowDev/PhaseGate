public class TaskEight{
public static void main(String...args){



int multiple = 1;
int sum = 0;
int sumTwo = 0;
for (int count = 1; count<=10; count ++){
if(count % 4 == 0){


multiple = 1;
sum =0;

for (int counter = 1; counter <= 5; counter ++){
multiple = multiple * count; 
sum = sum + multiple;

}
sumTwo = sumTwo +sum;

}
}

System.out.println(sumTwo);
}

}
