import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;


public class Main {
    private static List<Pal> pals = new ArrayList<>();
    private static List<String> soluciones = new ArrayList<>();
    private static List<String> path = new ArrayList<>();
    private static int limite = 1;

    public static void main(String[] args) {
        String scriptDir = System.getProperty("user.dir");
        try (BufferedReader br = new BufferedReader(new FileReader(scriptDir +
                "/src/main/resources/infopals.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] palText = line.split(" - ");
                pals.add(new Pal(palText[0], palText[1]));

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            String json = Files.readString(Paths.get(scriptDir + "/src/main/resources/breeding.json"));

            Gson gson = new Gson();
            Type Pal = new TypeToken<List<Pal>>(){}.getType();
            List<Pal> json1 = gson.fromJson(json, Pal);

            for (Pal pal : json1) {
                System.out.println(pal.getName() + " - " + pal.getPower());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}