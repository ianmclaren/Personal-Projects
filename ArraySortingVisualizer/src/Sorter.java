import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class Sorter extends JFrame{



    Sorter(){

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(700, 700);
        this.setLayout(new BorderLayout(0, 0));
        this.setResizable(false);
        this.setTitle("Array Sorting Visualizer");

        JPanel header = new JPanel();
        JPanel leftPanel = new JPanel();
        JPanel rightPanel = new JPanel();
        JPanel footer = new JPanel();
        JPanel center = new JPanel();

        header.setBackground(Color.GRAY);
        leftPanel.setBackground(Color.LIGHT_GRAY);
        rightPanel.setBackground(Color.LIGHT_GRAY);
        footer.setBackground(Color.GRAY);

        header.setPreferredSize(new Dimension(100, 100));
        leftPanel.setPreferredSize(new Dimension(50, 100));
        rightPanel.setPreferredSize(new Dimension(50, 100));
        footer.setPreferredSize(new Dimension(100, 100));

        center = new Array();

        this.add(header, BorderLayout.NORTH);
        this.add(leftPanel, BorderLayout.WEST);
        this.add(rightPanel, BorderLayout.EAST);
        this.add(footer, BorderLayout.SOUTH);
        this.add(center, BorderLayout.CENTER);

        
        this.setVisible(true);
    }
    
}
