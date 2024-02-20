package main.dataManagers;

import java.awt.*;
import java.io.File;
import java.io.IOException;

public class Pal {
    private String name;
    private int power;

    private String imagePath;

    public Pal() {}

    public Pal(String name, String power) {
        this.name = name;
        this.power = Integer.parseInt(power);
        this.imagePath = System.getProperty("user.dir") + "\\src\\images\\" + name + ".png";
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }
    public String getImage() {
        return this.imagePath;
    }
    public void setImagePath(String imagePath) {
        this.imagePath = imagePath;
    }

    @Override
    public String toString() {
        return name + " " + power;
    }
}