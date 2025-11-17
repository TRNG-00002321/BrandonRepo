//Transpose Matrix: Given a matrix, find its transpose (swap rows and columns).
//Matrix Addition: Add two matrices of the same dimensions.

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        int[][] nums = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        // need to transpose the column with the row
        // So I could move 00, 01, 02, with 00, 10, 20


        //store column, and swap with row. store the row and swap with column

        List<Integer> row = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums[i].length;j++){
                System.out.print(nums[i][j]+" ");

            }
            System.out.println();
        }


    }
}