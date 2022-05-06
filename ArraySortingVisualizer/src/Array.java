import java.awt.*;
import javax.swing.*;
import javax.swing.border.Border;
import java.awt.event.*;
import java.util.Random;
import java.util.concurrent.*;
import java.lang.Object;

public class Array extends JPanel implements ActionListener{
    
    JButton bubbleSortButton;
    JButton resetButton;
    JPanel[] bars;
    int[] heights;
    Border barBorder = BorderFactory.createLineBorder(Color.BLACK, 1);
    
    
    Array(){
        this.setLayout(null);

        /* Creating Buttons */
        bubbleSortButton = new JButton("Bubble");
        resetButton = new JButton("New Array");

        bubbleSortButton.setBounds(120, 420, 80, 30);
        resetButton.setBounds(0, 420, 100, 30);
        bubbleSortButton.setFocusable(false);
        resetButton.setFocusable(false);
        bubbleSortButton.addActionListener(this);
        resetButton.addActionListener(this);

        this.add(bubbleSortButton);
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

    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource() == bubbleSortButton){
            //Performing the bubble sort
            
            for(int i = 0; i < bars.length - 1; i++){
                for(int j = 0; j < bars.length - i - 1; j++){
                    if(bars[j].getHeight() > bars[j+1].getHeight()){
                                JPanel temp = new JPanel();
                                temp.setBounds(bars[j].getX(), bars[j].getY(), bars[j].getWidth(), bars[j].getHeight());
                                bars[j].setBounds(bars[j].getX(), bars[j+1].getY(), bars[j].getWidth(), bars[j+1].getHeight());
                                bars[j+1].setBounds(bars[j+1].getX(), temp.getY(), bars[j+1].getWidth(), temp.getHeight());
                                //this.updateUI();
                    }
                }
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
