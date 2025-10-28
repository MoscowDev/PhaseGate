
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class DayTwoTest{

@Test
public void testThattheNumberOfItemsIncrease(){
	DepriciationTask depreciate = new Depreciations();
	int result = depreciate.numberOfYears(50)
	assertEquals(result,50)


}
}