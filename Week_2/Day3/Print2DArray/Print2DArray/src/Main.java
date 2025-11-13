//Print a 2D Array: Write a program to initialize and
// print the elements of a given 2D integer array (matrix).

public class Main {
    public static void main(String[] args) {

        //2d array
        int nums[][] = {
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };

        //print out the 2d array

        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums[i].length;j++){
                System.out.println(nums[i][j]+" ");
            }
        }



    }

}
