public class PrimeRangeNumber{
	public static void main(String[] args){

	System.out.println();
	}
	
	public static Integer primeNumber(int number){
		
		int [] empty = {};
		
		for (int count = 0; count <= number.length; count++){
			if(number % count == 0){

			return number[count];
			}else if (number % count == 1){
			return number;
			}
		}
		}



} 






	

