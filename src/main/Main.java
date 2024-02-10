package main;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


public class Main {
    private static ArrayList<Pal> pals = new ArrayList<>();
    private static JSONArray breedings = new JSONArray();
    private static ArrayList<ArrayList<String>> soluciones = new ArrayList<>();

    public static void main(String[] args) {
        pals = loadPals();
        breedings = loadBreedings();
        mainLoop(lookAPal("vanwyrm"), lookAPal("foxparks"));
        System.out.println(soluciones);
    }

    public static ArrayList<ArrayList<String>> mainLoop(Pal initial, Pal objective){
        ArrayList<String> path = new ArrayList<>();
        int limite = 1;
        while (soluciones.isEmpty() && limite < 5) {
            lookpath(initial, objective, objective, path, limite);
            limite += 1;
            path.clear();
        }
        if (soluciones.isEmpty()){
            soluciones.clear();
            return null;
        }

        deleteRepetedSolutions();
        return soluciones;
    }

    public static ArrayList<Pal> loadPals() {
        String scriptDir = System.getProperty("user.dir");
        try (BufferedReader br = new BufferedReader(new FileReader(scriptDir +
                "/src/main/resources/infopals.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] palText = line.split(" - ");
                pals.add(new Pal(palText[0], palText[1]));
            }
            return pals;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }
    public static JSONArray loadBreedings() {
        String scriptDir = System.getProperty("user.dir");
        String json = null;
        try {
            json = Files.readString(Paths.get(scriptDir + "/src/main/resources/breeding.json"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        JSONObject data = new JSONObject(json);
        return data.getJSONArray("data");
    }

    public static void printBreeding(JSONArray breedings){
        for (int i = 0; i < breedings.length(); i++) {
            JSONObject breeding = breedings.getJSONObject(i);
            JSONObject parent1 = breeding.getJSONObject("parent1");
            JSONObject parent2 = breeding.getJSONObject("parent2");
            JSONObject child = breeding.getJSONObject("child");
        }
    }

    public static Pal lookAPal(String name){
        for (Pal pal : pals) {
            if (pal.getName().equalsIgnoreCase(name)) {
                return pal;
            }
        }
        return null;
    }

    public static ArrayList<JSONObject> lookAResult(Pal result) {
        ArrayList<JSONObject> results = new ArrayList<>();
        for (int i = 0; i < breedings.length(); i++) {
            JSONObject breeding = breedings.getJSONObject(i);
            JSONObject child = breeding.getJSONObject("child");
            if (child.get("name").toString().equalsIgnoreCase(result.getName())) {
                results.add(breeding);
            }
        }
        return results;
    }

    private static void lookACouple(Pal parent1, Pal parent2){
        for(int i=0; i < breedings.length(); i++){
            JSONObject breeding = breedings.getJSONObject(i);
            JSONObject parent1B = breeding.getJSONObject("parent1");
            JSONObject parent2B = breeding.getJSONObject("parent2");
            if(parent1.getName().equalsIgnoreCase(parent1B.get("name").toString()) &&
                    parent2.getName().equalsIgnoreCase(parent2B.get("name").toString())){
                JSONObject child = breeding.getJSONObject("child");
                System.out.println("Padres: " + parent1.getName() +
                        " y " + parent2.getName() +
                        " hijo: " + child.get("name"));
            }
        }
    }
    
    //cambiar parent por couple
    public static void lookpath(Pal initial, Pal objective, Pal current, ArrayList<String> path, int limite){
        if (path.isEmpty()){
            path.add(objective.getName());
        }
        ArrayList<JSONObject> parents = lookAResult(current);
        for (JSONObject couple : parents) {
            JSONObject parent1 = couple.getJSONObject("parent1");
            JSONObject parent2 = couple.getJSONObject("parent2");
            path.add(parent2.get("name").toString());
            path.add(parent1.get("name").toString());
            if (parent1 == parent2) continue;
            else if (parent1.get("name").toString().equalsIgnoreCase(initial.getName())) {
                soluciones.add(new ArrayList<>(path));
            } else if (parent2.get("name").toString().equalsIgnoreCase(initial.getName())){
                soluciones.add(new ArrayList<>(path));
            }
            else if(limite > 1) {
                lookpath(initial, objective, lookAPal(parent1.get("name").toString()), path, limite-1);
            }
            path.removeLast();
            path.removeLast();
        }
    }

    public static void deleteRepetedSolutions(){
        ArrayList<ArrayList<String>> solucionesfiltred = new ArrayList<>(soluciones);
        for (ArrayList<String> sol : soluciones) {
            for (ArrayList<String> sol2 : soluciones) {
                int i = 1;
                while (i < sol.size() - 1 && i < sol2.size()) {
                    if (sol2.get(i).equals(sol.get(i - 1)) && sol2.get(i - 1).equals(sol.get(i))) {
                        if (solucionesfiltred.contains(sol2) && solucionesfiltred.contains(sol)) {
                            solucionesfiltred.remove(sol2);
                        }
                    }
                    i += 2;
                }
            }
        }
        soluciones = new ArrayList<>(solucionesfiltred);
    }
}