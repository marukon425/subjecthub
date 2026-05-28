package GUI;
import java.util.concurrent.Flow;
import java.awt.FlowLayout;

import javax.swing.*;


public class Code18_5 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("初めてのGUI");
        JLabel label = new JLabel("HEllow World!!");
        JButton button = new JButton("おしてね");
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(label);
        frame.getContentPane().add(button);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 100);
        frame.setVisible(true);
    }
}
