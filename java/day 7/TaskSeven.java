public class TaskSeven{
public static void main(String...args){


int counter = 1;
int multiple = 1;
int sum = 0;
for (int count = 1; count<=10; count ++){
 if(count % 4 == 0){

for (counter = 1; counter <= 5; counter ++){
multiple = multiple * count; 
sum = sum + multiple;

}
System.out.println(sum);


multiple = 1;
sum =0;
}
}
}
}