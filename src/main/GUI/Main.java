//tanzee mono verde
package main.GUI;

import main.Manager;
import main.Pal;

import javax.swing.*;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import org.jdesktop.swingx.autocomplete.AutoCompleteDecorator;

public class Main {
    private JPanel MainPanel;
    private JPanel TitlePanel;
    private JPanel Button_Panel;
    private JPanel Combo1Panel;
    private JPanel Combo2Panel;
    private JPanel Path1Panel;
    private JPanel Path2Panel;
    private final CardLayout cardLayout = new CardLayout();
    private JPanel CenterPanel = new JPanel(cardLayout);
    private JButton BreedingPathButton;
    private JButton BreedingComboButton;
    private JButton PosibleParentsButton;
    private JTextPane WelcomeText;
    private JPanel BreedingPathPanel;
    private JPanel Welcome_Panel = new JPanel();
    private JPanel BreedingComboPanel;
    private JPanel PossibleParentsPanel;
    private JTextPane possibleParentsTextPane;
    private JButton TitleButton;
    private final Manager manager = new Manager();
    private JTextPane ComboTextResult;
    private JComboBox comboBox1;
    private JComboBox comboBox2;
    private JComboBox pathBox1;
    private JComboBox pathBox2;
    private JLabel ComboPal1;
    private JLabel ComboPal2;
    private JLabel ComboPal3;
    private JLabel path1Label;
    private JLabel path2Label;
    private JLabel Objective;
    private JLabel Initial;
    private JButton pathButton;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                JFrame frame = new JFrame("Main");
                Main main = new Main();
                frame.setContentPane(main.MainPanel);
                frame.setSize(1000,600);
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            }
        });
    }

    public Main() {
        setPanels();

        setButtons();

        setTexts();

        setComboBoxes();

        setStarterImages();

        setListeners();

        setComboResult();
    }

    public void setPanels(){
        MainPanel.add(CenterPanel, BorderLayout.CENTER);

        CenterPanel.add(Welcome_Panel, "WelcomeText");
        CenterPanel.add(BreedingPathPanel, "BreedingPath");
        CenterPanel.add(BreedingComboPanel, "BreedingCombo");
        CenterPanel.add(PossibleParentsPanel, "PosibleParents");

        Welcome_Panel.add(WelcomeText);
        Welcome_Panel.setBackground(Color.decode("#4F6280"));
        Welcome_Panel.setForeground(Color.WHITE);

        BreedingComboPanel.setBackground(Color.decode("#4F6280"));
        BreedingPathPanel.setBackground(Color.decode("#4F6280"));
        PossibleParentsPanel.setBackground(Color.decode("#4F6280"));

        possibleParentsTextPane.setBackground(Color.decode("#4F6280"));
        possibleParentsTextPane.setForeground(Color.WHITE);

        ComboTextResult.setBackground(Color.decode("#4F6280"));
        ComboTextResult.setForeground(Color.WHITE);

        Combo1Panel.setBackground(Color.decode("#4F6280"));
        Combo2Panel.setBackground(Color.decode("#4F6280"));
        Path1Panel.setBackground(Color.decode("#4F6280"));
        Path2Panel.setBackground(Color.decode("#4F6280"));
    }

    public void setButtons(){
        TitleButton.setText("PalworldBreeder");
        TitleButton.setFont(new Font("Arial", Font.BOLD, 24));
        TitleButton.setForeground(Color.WHITE);

        pathButton.setBackground(Color.decode("#4F6280"));

        BreedingComboButton.setForeground(Color.WHITE);
        BreedingPathButton.setForeground(Color.WHITE);
        PosibleParentsButton.setForeground(Color.WHITE);
        pathButton.setForeground(Color.WHITE);
    }

    public void setTexts(){
        WelcomeText.setBackground(Color.decode("#4F6280"));
        WelcomeText.setForeground(Color.WHITE);

        StyledDocument doc = WelcomeText.getStyledDocument();
        SimpleAttributeSet center = new SimpleAttributeSet();
        StyleConstants.setAlignment(center, StyleConstants.ALIGN_CENTER);
        doc.setParagraphAttributes(0, doc.getLength(), center, false);

        WelcomeText.setText("""
                Welcome to PalworldBreeder
                This is a tool to help you find the best way to breed your Palworld creatures.
                You can find the best path to breed a specific creature
                the best combination of creatures to breed a specific creature
                and the possible parents of a specific creature.
                To start, select one of the options of the left.""");

        Initial.setBackground(Color.decode("#4F6280"));
        Initial.setForeground(Color.WHITE);

        Objective.setBackground(Color.decode("#4F6280"));
        Objective.setForeground(Color.WHITE);
    }

    public void setComboBoxes(){
        comboBox1.setBackground(Color.decode("#4F6280"));
        comboBox1.setForeground(Color.WHITE);

        comboBox2.setBackground(Color.decode("#4F6280"));
        comboBox2.setForeground(Color.WHITE);

        pathBox1.setBackground(Color.decode("#4F6280"));
        pathBox1.setForeground(Color.WHITE);

        pathBox2.setBackground(Color.decode("#4F6280"));
        pathBox2.setForeground(Color.WHITE);

        for (Pal pal : manager.listOfPals()) {
            comboBox1.addItem(pal.getName());
            comboBox2.addItem(pal.getName());
            pathBox1.addItem(pal.getName());
            pathBox2.addItem(pal.getName());
        }

        AutoCompleteDecorator.decorate(comboBox1);
        AutoCompleteDecorator.decorate(comboBox2);
        AutoCompleteDecorator.decorate(pathBox1);
        AutoCompleteDecorator.decorate(pathBox2);

        ComboTextResult.setText("Lamball");
        StyledDocument doc = ComboTextResult.getStyledDocument();
        SimpleAttributeSet center = new SimpleAttributeSet();
        StyleConstants.setAlignment(center, StyleConstants.ALIGN_CENTER);
        doc.setParagraphAttributes(0, doc.getLength(), center, false);
    }

    public void setStarterImages(){
        String path = System.getProperty("user.dir") + "\\src\\images\\Lamball.png";
        ImageIcon icon = new ImageIcon(path);
        ComboPal1.setIcon(icon);

        icon = new ImageIcon(path);
        ComboPal2.setIcon(icon);

        icon = new ImageIcon(path);
        path1Label.setIcon(icon);

        icon = new ImageIcon(path);
        path2Label.setIcon(icon);

        ComboPal3.setIcon(icon);

    }

    public void setComboResult(){

    }
    public void setListeners(){
        comboBox1.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    Pal PalSelected = manager.lookAPal((String) comboBox1.getSelectedItem());
                    String path = System.getProperty("user.dir") + "\\src\\images\\" + PalSelected.getName() + ".png";
                    ImageIcon icon = new ImageIcon(path);
                    ComboPal1.setIcon(icon);
                    Pal pal1 = manager.lookAPal((String) comboBox1.getSelectedItem());
                    Pal pal2 = manager.lookAPal((String) comboBox2.getSelectedItem());
                    Pal resultado = manager.lookACouple(pal1,pal2);
                    icon = new ImageIcon(resultado.getImage());
                    ComboPal3.setIcon(icon);
                    ComboTextResult.setText(resultado.getName());
                }
            }
        });
        comboBox2.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    Pal PalSelected = manager.lookAPal((String) comboBox2.getSelectedItem());
                    String path = System.getProperty("user.dir") + "\\src\\images\\" + PalSelected.getName() + ".png";
                    ImageIcon icon = new ImageIcon(path);
                    ComboPal2.setIcon(icon);
                    Pal pal1 = manager.lookAPal((String) comboBox1.getSelectedItem());
                    Pal pal2 = manager.lookAPal((String) comboBox2.getSelectedItem());
                    Pal resultado = manager.lookACouple(pal1,pal2);
                    icon = new ImageIcon(resultado.getImage());
                    ComboPal3.setIcon(icon);
                    ComboTextResult.setText(resultado.getName());
                }
            }
        });

        pathBox1.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    Pal PalSelected = manager.lookAPal((String) pathBox1.getSelectedItem());
                    String path = System.getProperty("user.dir") + "\\src\\images\\" + PalSelected.getName() + ".png";
                    ImageIcon icon = new ImageIcon(path);
                    path1Label.setIcon(icon);
                }
            }
        });

        pathBox2.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    Pal PalSelected = manager.lookAPal((String) pathBox2.getSelectedItem());
                    String path = System.getProperty("user.dir") + "\\src\\images\\" + PalSelected.getName() + ".png";
                    ImageIcon icon = new ImageIcon(path);
                    path2Label.setIcon(icon);
                }
            }
        });
        BreedingPathButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cardLayout.show(CenterPanel, "BreedingPath");
            }
        });

        BreedingComboButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cardLayout.show(CenterPanel, "BreedingCombo");
            }
        });
        PosibleParentsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cardLayout.show(CenterPanel, "PosibleParents");
            }
        });

        TitleButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                cardLayout.show(CenterPanel, "WelcomeText");
            }
        });
    }
}