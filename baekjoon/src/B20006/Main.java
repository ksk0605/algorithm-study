import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String... agrs) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        List<Integer> ints = Arrays.stream(input.split(" ")).map(token -> Integer.parseInt(token))
                .collect(Collectors.toList());
        int playerLength = ints.get(0);
        int limit = ints.get(1);

        var rooms = new Rooms(limit);

        for (int i = 0; i < playerLength; i++) {
            String[] tokens = br.readLine().split(" ");
            int level = Integer.parseInt(tokens[0]);
            String name = tokens[1];
            var p = new Player(level, name);
            if (rooms.canIn(p)) {
                rooms.in(p);
            } else {
                rooms.create(p);
            }
        }

        for (var r : rooms.rooms) {
            System.out.print(r);
        }
    }

    static class Player {
        public String name;
        public int level;

        public Player(int level, String name) {
            this.name = name;
            this.level = level;
        }

        @Override
        public String toString() {
            return "Player [name=" + name + ", level=" + level + "]";
        }
    }

    static class Room {
        public List<Player> players = new ArrayList<>();
        int max;
        int firstLevel;

        public Room(int max) {
            this.max = max;
        }

        public void add(Player p) {
            if (players.size() == 0) {
                this.firstLevel = p.level;
            }
            players.add(p);
        }

        public boolean canIn(Player p) {
            if (players.size() < max && p.level <= firstLevel + 10 && p.level >= firstLevel - 10) {
                return true;
            }
            return false;
        }

        public void in(Player p) {
            players.add(p);
        }

        public boolean isStarted() {
            if (players.size() == max) {
                return true;
            }
            return false;
        }

        @Override
        public String toString() {
            players.sort((p1, p2) -> p1.name.compareTo(p2.name));

            var sb = new StringBuffer();

            if (isStarted()) {
                sb.append("Started!\n");
            } else {
                sb.append("Waiting!\n");
            }
            for (var p : players) {
                sb.append(p.level + " " + p.name + "\n");
            }
            return sb.toString();
        }
    }

    static class Rooms {
        public List<Room> rooms = new ArrayList<>();
        int max;

        public Rooms(int max) {
            this.max = max;
        }

        public void create(Player p) {
            var r = new Room(max);
            r.add(p);
            rooms.add(r);
        }

        public boolean canIn(Player p) {
            if (rooms.size() == 0)
                return false;

            for (var r : rooms) {
                if (r.canIn(p)) {
                    return true;
                }
            }
            return false;
        }

        public void in(Player p) {
            for (var r : rooms) {
                if (r.canIn(p)) {
                    r.in(p);
                    return;
                }
            }
        }
    }
}