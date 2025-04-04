package B20055;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    /*
     * 벨트는 매 반복마다 한칸씩 이동한다. 
     * 벨트 위 로봇은 각자 위치가 있고 갈 수 있으면 매 반복마다 한 칸씩 이동한다. 
     * 벨트는 칸마다 내구도가 있다. 
     * 1번은 올리고 n번은 내린다. 
     * 3 2
        1 2 1 2 1 2

        2 1 2 1 2 1
        1 1 2 1 2 1 

        0 1 0 2 1 2 
     */

    public static void main(String... args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        var tokens = bf.readLine().split(" ");

        int n = Integer.parseInt(tokens[0]);
        int k = Integer.parseInt(tokens[1]);

        List<Integer> as = Arrays.stream(bf.readLine().split(" ")).map(t -> Integer.parseInt(t)).collect(Collectors.toList());

        List<Section> sections = new ArrayList<>();
        for (var d : as) { 
            Section section = new Section(d);
            sections.add(section);
        }
        Belt belt = new Belt(sections);
        Conveyor conveyor = new Conveyor(belt, k);

        int step = conveyor.run();
        System.out.println(step);
    }

    static class Conveyor { 
        int step; 
        Belt belt; 
        int limit;
        int start; 
        int end;

        public Conveyor(Belt belt, int k) { 
            step = 0;
            this.belt = belt;
            this.limit = k;
            start = 0;
            end = belt.getSize() / 2 - 1;
        }

        public int run(){
            while (belt.getLimitCount() < limit) {
                step++;
                // System.out.println("current step: " + step);
                belt.go();
                belt.moveRobots();
                if (belt.canOn(start)) {
                    belt.on(start, new Robot());
                }
                // System.out.println("current belt count: " + belt.getLimitCount());
            }
            return step;
        }
    }

    static class Belt{ 
        // 1 2 3 4 5 6 
        // 6 1 2 3 4 5
        List<Section> sections; 

        public Belt(List<Section> sections){ 
            this.sections = sections;
        }

        public void moveRobots() {
            for (int i = (sections.size() / 2 - 2); i>=0; i--){ 
                if (sections.get(i).haveRobot() && sections.get(i+1).canOn()){ 
                    Robot r = sections.get(i).out();
                    sections.get(i+1).on(r);
                }
            }
            if (sections.get(sections.size() / 2 - 1).haveRobot()){ 
                sections.get(sections.size() / 2 - 1).out();
            }
        }

        public void go() {
            List<Section> newSections = new ArrayList<>();
            int last = sections.size()-1;
            newSections.add(sections.get(last));
            for(int i = 0; i<sections.size()-1; i++){ 
                newSections.add(sections.get(i));
            }
            this.sections = newSections;

            if (sections.get(sections.size() / 2 - 1).haveRobot()){ 
                sections.get(sections.size() / 2 - 1).out();
            }
        }

        public void on(int sectionNumber, Robot robot) {
            sections.get(sectionNumber).on(robot);
        }

        public boolean canOn(int sectionNumber) {
            Section section = sections.get(sectionNumber);
            return section.canOn();
        }

        public int getSize() {
            return sections.size();
        }

        public int getLimitCount() { 
            int count = 0;
            for (var s : sections) {
                if (s.durability == 0) { 
                    count++;
                }
            }
            return count;
        }
    }

    static class Section { 
        int durability;
        Robot robot;

        public Section(int d) { 
            this.durability = d;
        }

        public boolean haveRobot() {
            return this.robot != null;
        }

        public boolean canOn() {
            return durability > 0 && robot == null;
        }

        public void on(Robot robot) { 
            this.robot = robot;
            this.durability -= 1;
        }

        public Robot out() { 
            Robot r = this.robot;
            this.robot = null;
            return r;
        }
    }

    static class Robot { 

    }
}
