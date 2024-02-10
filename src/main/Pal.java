package main;

public class Pal {
    private String name;
    private int power;

    public Pal() {}

    public Pal(String name, String power) {
        this.name = name;
        this.power = Integer.parseInt(power);
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
}