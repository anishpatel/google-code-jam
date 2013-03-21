import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

// 
public class B
{
	static String FILE_NAME = "B-sample";
//	static String FILE_NAME = "B-small-attempt0";
//	static String FILE_NAME = "B-large";
	
	
	
	public static void main(String[] args)
	{
		Scanner sc = null;
		PrintWriter pw = null;
		try {
			sc = new Scanner(new File(FILE_NAME+".in"));
			pw = new PrintWriter(FILE_NAME+".out");
			int numCases = sc.nextInt();
			for (int c = 1; c <= numCases; c++) {
				/* CASE BEGINS */
				
				// get input
				
				
				// process
//				int result = ;
				
				// output
//				pw.printf("Case #%d: %d\n", c, result);
				
				/* CASE ENDS */
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} finally {
			sc.close();
			pw.close();
		}
	}
}
