//Sum of Elements: Calculate the sum of all elements in a 2D array.
//Find Maximum/Minimum: Find the maximum or minimum element within a 2D array.

public class Main {
    public static void main(String[] args) {

        int[][] nums = {
                {25, 33, 22},
                {14, 8, 37},
                {21, 2, 28}
        };

        int sum = 0;
        //find the sum of all elements in a 2d array
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums[i].length;j++){
                sum += (nums[i][j]);
            }
        }

        int smallestNumber = nums[0][0];
        //find the maximum element in the 2d array
        for(int x=0;x<nums.length;x++){
            for(int y=0;y<nums[x].length;y++){
                if(nums[x][y]<smallestNumber){
                    smallestNumber = nums[x][y];
                }
            }
        }

        System.out.println("The sum is: "+sum);
        System.out.println("The smallest number is: "+smallestNumber);

    }
}
