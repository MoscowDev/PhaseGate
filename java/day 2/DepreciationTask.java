
public class DepreciationTask{



	public static int numberOfItems(int numberOfItems ){
		int fixedPrice = 50000 * numberOfItems;
		int count = 0;
		double rate = 0.08;
		
		while(fixedPrice > 0.0){
		fixedPrice /= rate;
		count += 1;

		
		
}
 return count;		
				
System.out.print(fixedPrice);



}
}


