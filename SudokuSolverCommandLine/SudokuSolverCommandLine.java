public class Sudoku {
    public static void main(String[] args) {
        //System.out.println("Testing");
        int[][] board = { 
        {0, 1, 0, 0, 0, 0, 0, 4, 0}, 
        {0, 0, 4, 0, 2, 0, 0, 0, 0}, 
        {3, 0, 8, 0, 7, 0, 0, 0, 0}, 
        {2, 0, 1, 0, 0, 0, 0, 0, 0}, 
        {0, 0, 0, 0, 0, 0, 4, 9, 0},
        {0, 0, 0, 1, 6, 0, 0, 3, 2}, 
        {5, 6, 0, 0, 0, 0, 7, 0, 0}, 
        {4, 0, 2, 5, 0, 0, 6, 0, 0},
        {0, 0, 0, 0, 3, 0, 0, 0, 0} 
        };

        System.out.println("Unsolved Puzzle:");
        print_board(board);
        
        if (valid_board(board) == true){
            System.out.println("Valid board");
        }
        else{
            System.out.println("Invalid board. Please modify the input board and try again");
        }

        int[] startpoint = find_zero(board);
        if(startpoint == null){
            System.out.println("Input is a valid solution");
        }
        else{
            if(backtracking_algo(board, startpoint[0], startpoint[1]) == true){
                System.out.println("Solution Found:");
                print_board(board);
            }else{
                System.out.println("No Solution Found. Please modify the puzzle and try again.");
                print_board(board);
            }
        }
    }
    
    //Performs the recursive backtracking to solve the puzzle
    public static boolean backtracking_algo(int[][] board, int x, int y) {
        //Finding the first zero for a startpoint
        for(int val = 1; val < 10; val++){
            board[x][y] = val;
            //If the value in this spot doesn't conflict with any existing numbers
            if(check_spot(board, x, y) == true){
                int[] next_location = find_zero(board);
                //If the sudoku puzzle has no zeroes, puzzle is complete
                if(next_location == null){
                    return true;
                }else{
                    //Recursively call this function and see if it reaches the end of the puzzle
                    if(backtracking_algo(board, next_location[0], next_location[1]) == true){
                        return true;
                    }else{
                        board[x][y] = 0;
                    }
                }
            }else{
                //If value does conflict, reset it to 0
                board[x][y] = 0;
            }
        }
        
        return false;
    }

    //Finds first 0 spot
    public static int[] find_zero(int[][] board){
        
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] == 0){
                    int[] location = {i, j};
                    return location;
                }
            }
        }
        return null;
    }

    //Checks if spot is valid
    public static boolean check_spot(int[][] board, int i, int j) {
        //Checking row
        int count = 0;
        int row;
        int col;
        for(col = 0; col < 9; col++){
            if(board[i][j] == board[i][col]){
                count++;
            }
        }
        //Checking column
        for(row = 0; row < 9; row++){
            if(board[i][j] == board[row][j]){
                count++;
            }
        }
        //Checking box
        for(row = (i / 3) * 3; row < ((i / 3) * 3) + 3; row++){
            for(col = (j / 3) * 3; col < ((j / 3) * 3) + 3; col++){
                if(board[i][j] == board[row][col]){
                    count++;
                }
            }
        }

        if(count == 3){
            return true;
        }
        return false;    
    }

    //Check if board is valid
    public static boolean valid_board(int[][] board){
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(board[i][j] != 0){
                    if(check_spot(board, i, j) == false){
                        return false;
                    }
                }
            }
        }
        return true;
    }

    //Reset the board to empty
    public static int[][] reset_board(){
        int[][] board = new int[9][9];
        return board;
    }

    //Print board
    public static void print_board(int[][] board){
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                System.out.print(board[i][j]);
                System.out.print(" ");
                //If it's at the edge of a box
                if(j % 3 == 2 && j != 8){
                    System.out.print("| ");
                }
            }
            System.out.println("");
            //If it's at the edge of a box
            if(i % 3 == 2 && i != 8){
                System.out.println("----------------------");
            }
        }
    }
}
