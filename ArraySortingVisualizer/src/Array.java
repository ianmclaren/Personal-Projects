import java.awt.*;
import javax.swing.*;
import javax.swing.border.Border;
import java.awt.event.*;
import java.util.Random;
import java.util.concurrent.*;
import java.lang.Object;

public class Array extends JPanel implements ActionListener{
    
    JButton bubbleSortButton;
    JButton quickSortButton;
    JButton insertionSortButton;
    JButton resetButton;
    JPanel[] bars;
    int[] heights;
    Border barBorder = BorderFactory.createLineBorder(Color.BLACK, 1);
    
    
    Array(){
        this.setLayout(null);

        /* Creating Buttons */
        bubbleSortButton = new JButton("Bubble");
        quickSortButton = new JButton("Quick");
        insertionSortButton = new JButton("Insertion");
        resetButton = new JButton("New Array");

        bubbleSortButton.setBounds(150, 420, 90, 30);
        quickSortButton.setBounds(250, 420, 90, 30);
        insertionSortButton.setBounds(350, 420, 90, 30);
        resetButton.setBounds(0, 420, 100, 30);

        bubbleSortButton.setFocusable(false);
        quickSortButton.setFocusable(false);
        insertionSortButton.setFocusable(false);
        resetButton.setFocusable(false);

        bubbleSortButton.addActionListener(this);
        quickSortButton.addActionListener(this);
        insertionSortButton.addActionListener(this);
        resetButton.addActionListener(this);

        this.add(bubbleSortButton);
        this.add(quickSortButton);
        this.add(insertionSortButton);
        this.add(resetButton);


        /* Creating the array bars */
        heights = new int[20];
        heights = randomizeArray(20);

        bars = new JPanel[20];
        for(int i = 0; i < 20; i++){
            bars[i] = new JPanel();
            bars[i].setBackground(Color.CYAN);
            bars[i].setBounds((i * 29), (400 - heights[i]), 29, heights[i]);
            bars[i].setBorder(barBorder);
            this.add(bars[i]);
        }
        
    }

    
    public static int[] randomizeArray(int length){
        Random rd = new Random();
        int[] arr = new int[length];
        for(int i = 0; i < length; i++){
            arr[i] = rd.nextInt(400);
        }
        return arr;
    }


    public static void swap(JPanel bars[], int i, int j){
        JPanel temp = new JPanel();
        temp.setBounds(bars[i].getX(), bars[i].getY(), bars[i].getWidth(), bars[i].getHeight());
        bars[i].setBounds(bars[i].getX(), bars[j].getY(), bars[i].getWidth(), bars[j].getHeight());
        bars[j].setBounds(bars[j].getX(), temp.getY(), bars[j].getWidth(), temp.getHeight());
    }


    public static int partition(JPanel bars[], int low, int high){
        JPanel pivot = new JPanel();
        //Setting the pivot to the last element because we know the array is randomized. 
        //This means setting the pivot to the last element won't negatively affect runtime.
        pivot.setBounds(bars[high].getX(), bars[high].getY(), bars[high].getWidth(), bars[high].getHeight());
        
        int i = (low - 1);
        for(int j = low; j <= high - 1; j++)
        {
            if (bars[j].getHeight() < pivot.getHeight())
            {
                i++;
                swap(bars, i, j);
            }
        }

        swap(bars, i + 1, high);
        return (i + 1);
    }

    public static void quickSort(JPanel bars[], int low, int high){
        if(low < high){
            int partition = partition(bars, low, high);
            quickSort(bars, low, partition - 1);
            quickSort(bars, partition + 1, high);
        }
    }


    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource() == bubbleSortButton){
            //Performing the bubble sort
            
            for(int i = 0; i < bars.length - 1; i++){
                for(int j = 0; j < bars.length - i - 1; j++){
                    if(bars[j].getHeight() > bars[j+1].getHeight()){
                        swap(bars, j, j+1);
                    }
                }
            }
        }
        
        if(e.getSource() == quickSortButton){
            quickSort(bars, 0, 19);
        }
        
        if(e.getSource() == insertionSortButton){
            for(int i = 1; i < bars.length; i++){
                JPanel temp = new JPanel();
                temp.setBounds(bars[i].getX(), bars[i].getY(), bars[i].getWidth(), bars[i].getHeight());
                int j = i - 1;

                while(j >= 0 && bars[j].getHeight() > temp.getHeight()){
                    bars[j+1].setBounds(bars[j+1].getX(), bars[j].getY(), bars[j+1].getWidth(), bars[j].getHeight());
                    j = j - 1;
                }
                bars[j+1].setBounds(bars[j+1].getX(), temp.getY(), bars[j+1].getWidth(), temp.getHeight());
            }
        }

        if(e.getSource() == resetButton){
            heights = new int[20];
            heights = randomizeArray(20);
            
            for(int i = 0; i < 20; i++){
                bars[i].setBackground(Color.CYAN);
                bars[i].setBounds((i * 29), (400 - heights[i]), 29, heights[i]);
                bars[i].setBorder(barBorder);
                this.add(bars[i]);
            }
        }
        
    }

}
