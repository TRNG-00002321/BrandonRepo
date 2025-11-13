// Row/Column Sums: Calculate the sum of elements for each
// individual row and each individual column in a 2D array.

public class Main {
    public static void main(String[] args) {

        int[][] nums = {
                {42, 13, 26},
                {65, 23, 27},
                {17, 21, 22}
        };


        //calculate the sum of each row
        int rowSum = 0;

        int row = 0;
        for(int i = 0; i < nums.length; i++){
            row++;
            for(int j = 0; j < nums[i].length; j++){
                rowSum += nums[i][j];
            }
            System.out.println("Row "+row+" = " + rowSum);
            rowSum = 0;
        }

        // calculate the sum of each column
        int colSum = 0;
        int col = 0;
        // i need j to increment more slowly
        // needs to look like [00]-[01]-[02]-[10]-[11]-[12]-etc
        for(int j = 0; j < nums[0].length; j++){
            col++;
            for(int i = 0; i < nums.length; i++){
                colSum += nums[i][j];
            }
            System.out.println("Col "+col+" = " + colSum);
            colSum = 0;
        }
    }
}