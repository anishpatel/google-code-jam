import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

// 
public class C
{
	static String FILE_NAME = "C-sample";
//	static String FILE_NAME = "C-small-attempt0";
//	static String FILE_NAME = "C-large";
	
	
	
	public static void main(String[] args)
	{
		Scanner sc = null;
		PrintWriter pw = null;
		try {
			sc = new Scanner(new File(FILE_NAME+".in"));
			pw = new PrintWriter(FILE_NAME+".out");
			int nCases = sc.nextInt();
			for (int c = 1; c <= nCases; c++) {
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
