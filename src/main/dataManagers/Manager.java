package main.dataManagers;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.LinkedList;


public class Manager {
    private static ArrayList<Pal> pals = new ArrayList<>();
    private static JSONArray breedings = new JSONArray();
    private static ArrayList<ArrayList<Pal>> soluciones = new ArrayList<>();

    public Manager() {
        pals = loadPals();
        breedings = loadBreedings();
    }

    public LinkedList<Pal> listOfPals(){
        LinkedList<Pal> palsToSend = new LinkedList<>(pals);
        return palsToSend;
    }

    public ArrayList<ArrayList<Pal>> mainLoop(Pal initial, Pal objective){
        soluciones.clear();
        ArrayList<Pal> path = new ArrayList<>();
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

    public ArrayList<Pal> loadPals() {
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
    public JSONArray loadBreedings() {
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

    public Pal lookAPal(String name){
        for (Pal pal : pals) {
            if (pal.getName().equalsIgnoreCase(name)) {
                return pal;
            }
        }
        return null;
    }

    public ArrayList<JSONObject> lookAResult(Pal result) {
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

    public Pal lookACouple(Pal parent1, Pal parent2){
        for(int i=0; i < breedings.length(); i++){
            JSONObject breeding = breedings.getJSONObject(i);
            JSONObject parent1B = breeding.getJSONObject("parent1");
            JSONObject parent2B = breeding.getJSONObject("parent2");
            if(parent1.getName().equalsIgnoreCase(parent1B.get("name").toString()) &&
                    parent2.getName().equalsIgnoreCase(parent2B.get("name").toString())){
                JSONObject child = breeding.getJSONObject("child");
                return lookAPal(child.get("name").toString());
            }
        }
        return null;
    }

    public ArrayList<ArrayList<Pal>> lookParents(Pal child){
        ArrayList<ArrayList<Pal>> parents = new ArrayList<>();
        for(int i=0; i < breedings.length(); i++){
            JSONObject breeding = breedings.getJSONObject(i);
            JSONObject childB = breeding.getJSONObject("child");
            if(child.getName().equalsIgnoreCase(childB.get("name").toString())){
                JSONObject parent1 = breeding.getJSONObject("parent1");
                JSONObject parent2 = breeding.getJSONObject("parent2");
                ArrayList<Pal> couple = new ArrayList<>();
                couple.add(lookAPal(parent1.get("name").toString()));
                couple.add(lookAPal(parent2.get("name").toString()));
                parents.add(couple);
            }
        }
        return parents;
    }
    
    //cambiar parent por couple
    public void lookpath(Pal initial, Pal objective, Pal current, ArrayList<Pal> path, int limite){
        if (path.isEmpty()){
            path.add(objective);
        }
        ArrayList<JSONObject> parents = lookAResult(current);
        for (JSONObject couple : parents) {
            JSONObject parent1 = couple.getJSONObject("parent1");
            JSONObject parent2 = couple.getJSONObject("parent2");
            path.add(lookAPal(parent1.get("name").toString()));
            path.add(lookAPal(parent2.get("name").toString()));
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

    public void deleteRepetedSolutions(){
        ArrayList<ArrayList<Pal>> solucionesfiltred = new ArrayList<>(soluciones);
        for (ArrayList<Pal> sol : soluciones) {
            for (ArrayList<Pal> sol2 : soluciones) {
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