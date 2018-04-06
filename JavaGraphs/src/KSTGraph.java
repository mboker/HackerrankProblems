import java.io.File;
import java.util.*;
import java.util.concurrent.ConcurrentSkipListSet;

public class KSTGraph {

    public static void main(String[] args) throws Exception{
        File file = new File("tests/KSTGraph.txt");
        Scanner scanner = new Scanner(file);
        String[] gNodesEdges = scanner.nextLine().split(" ");
        int gNodes = Integer.parseInt(gNodesEdges[0].trim());
        int gEdges = Integer.parseInt(gNodesEdges[1].trim());


        List<Edge> edges = new ArrayList<>();
        Map<Integer, List<Edge>> graph = new HashMap<>();
        for (int i = 1; i <= gNodes; i++){
            graph.put(i, new ArrayList<>());
        }

        Integer from, to, weight;
        for (int gItr = 0; gItr < gEdges; gItr++) {
            String[] gFromToWeight = scanner.nextLine().split(" ");
            from = Integer.parseInt(gFromToWeight[0].trim());
            to = Integer.parseInt(gFromToWeight[1].trim());
            weight = Integer.parseInt(gFromToWeight[2].trim());

            Edge edge = new Edge(from, to, weight);
            graph.get(from).add(edge);
            graph.get(to).add(edge);
            edges.add(edge);
        }
        Collections.sort(edges);
        Edge start = edges.get(0);
        System.out.println(getMstWeight(graph, start, gNodes));
    }

    private static Integer getMstWeight(Map<Integer, List<Edge>> graph,
                                        Edge start, int numNodes){
        Integer totalWeight = 0;
        Set<Edge> currentEdges = new ConcurrentSkipListSet<>();
        Set<Integer> connected = new HashSet<>();

        currentEdges.addAll(graph.get(start.getSource()));
        currentEdges.addAll(graph.get(start.getDest()));
        connected.add(start.getDest());
        connected.add(start.getSource());
        totalWeight = start.getWeight();

        Iterator<Edge> iterator = currentEdges.iterator();
        while ( connected.size() < numNodes){
            Edge currentEdge = iterator.next();
            if (! (connected.contains(currentEdge.getDest()) && connected.contains(currentEdge.getSource()) )) {
                connected.add(currentEdge.getDest());
                connected.add(currentEdge.getSource());
                currentEdges.addAll(graph.get(currentEdge.getSource()));
                currentEdges.addAll(graph.get(currentEdge.getDest()));
                totalWeight += currentEdge.getWeight();
                iterator.remove();
                iterator = currentEdges.iterator();
            } else {
                iterator.remove();
            }
        }
        return totalWeight;
    }

    private static class Edge implements Comparable<Edge>{
        private Integer dest;
        private Integer weight;
        private Integer source;

        public Edge(Integer source, Integer dest, Integer weight){
            this.source = source;
            this.dest = dest;
            this.weight = weight;
        }

        public Integer getSource(){ return source; }
        public Integer getDest(){ return dest; }
        public Integer getWeight(){ return weight; }

        @Override
        public int compareTo(Edge other){
            int weightCompare = weight.compareTo(other.getWeight());
            if (weightCompare == 0){
                Integer thisValue = dest*17 + source*23;
                Integer otherValue = other.getDest()*17 + other.getSource()*23;
                return thisValue.compareTo(otherValue);
            }
            return weightCompare;
        }
    }
}