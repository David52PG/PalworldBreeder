package main.GUI;

import main.Manager;
import main.Pal;

import javax.swing.*;
import java.awt.*;
import java.util.LinkedList;

public class ComboBox extends JComboBox<String> {

    public ComboBox(Manager manager) {
        super();
        setFont(new Font("Arial", Font.PLAIN, 14));
        setForeground(Color.BLACK);
        for (Pal item : manager.listOfPals()){
            this.addItem(item.getName());
        }
        setBackground(Color.WHITE);
    }
}
