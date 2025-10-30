public class PPerfectSquare{


public static boolean returnPerfectSquare(int  num){

	boolean result = false;
    if (num < 0){
	result = false;
	}
    for (int count = 0; count * count <= num; count++) {
        if (count * count == num) {
            result = true;
        }
else{

    result = false;
    }

	
}
return result;
}

}


