import java.io.File;
import java.util.*;

public class EvenTree {


    public static void main(String[] args) throws Exception {
        File file = new File("tests/EvenTree.txt");
        Scanner scanner = new Scanner(file);
        String[] treeNodesEdges = scanner.nextLine().split(" ");
        int treeNodes = Integer.parseInt(treeNodesEdges[0].trim());
        int treeEdges = Integer.parseInt(treeNodesEdges[1].trim());

        Map<Integer, List<Integer>> tree = new HashMap<>();

        for (int treeItr = 0; treeItr < treeEdges; treeItr++) {
            String[] treeFromTo = scanner.nextLine().split(" ");
            Integer treeFrom = Integer.parseInt(treeFromTo[0].trim());
            Integer treeTo = Integer.parseInt(treeFromTo[1].trim());
            if (!tree.containsKey(treeTo)){
                tree.put(treeTo, new ArrayList<Integer>());
            }
            tree.get(treeTo).add(treeFrom);
        }

        System.out.println(getMaxRemovals(tree, 1).get("removals"));
    }

    private static Map<String,Integer> getMaxRemovals(Map<Integer, List<Integer>> tree, Integer root){
        Integer total = 0;
        Integer leftover = 0;
        Map<String, Integer> returnMap = new HashMap<>();
        if (!tree.containsKey(root)){
            returnMap.put("leftover", 1);
            returnMap.put("removals", 0);
            return returnMap;
        }
        for (Integer child : tree.get(root)){
            returnMap = getMaxRemovals(tree, child);
            total += returnMap.get("removals");
            leftover += returnMap.get("leftover");
            if (returnMap.get("leftover") == 0){
                total += 1;
            }
        }
        if (leftover % 2 == 1){
            leftover = 0;
        } else {
            leftover += 1;
        }
        returnMap.put("removals", total);
        returnMap.put("leftover", leftover);
        return returnMap;
    }
}
