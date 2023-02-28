import java.util.LinkedList;
import java.util.Queue;

public class Grafo {

    static int[][] Matrix_ady_no = { // 0, 1, 2, 3, 4
                                  /*0*/{0, 1 ,0 ,0, 1},
                                  /*1*/{1, 0 ,1 ,1, 1},
                                  /*2*/{0, 1 ,0 ,1, 0},
                                  /*3*/{0, 1 ,1 ,0, 1},
                                  /*4*/{1, 1 ,0 ,1, 0}};
    static int[][] Matrix_ady = { // 0, 1, 2, 3, 4, 5
                               /*0*/{0, 1 ,0 ,1, 0, 0},
                               /*1*/{0, 0 ,0 ,0, 1, 0},
                               /*2*/{0, 0 ,0 ,0, 1, 1},
                               /*3*/{0, 1 ,0 ,0, 0, 0},
                               /*4*/{0, 0 ,0 ,1, 0, 0},
                               /*5*/{0, 0 ,0 ,0, 0, 1}};

    public static LinkedList<Vertices> lista = new  LinkedList<Vertices>();
    public static boolean[] visitado = new boolean[Matrix_ady_no.length];

    public static void llenarLista(){
        for(int i = 0; i < Matrix_ady_no.length ;i++){
            Vertices temp = new Vertices(i);
            for(int j = 0; j < Matrix_ady_no.length ; j++){
                if (Matrix_ady_no[i][j] == 1){
                    temp.adyacentes.add(j);
                }
            }
            lista.add(temp);
        }
    }
    public static void mostrarLista(){
        for(Vertices vertice: lista){
            System.out.print(vertice.getDato());
            for(Integer adyacente: vertice.getAdyacentes()){
                System.out.print("->"+adyacente);
            }
            System.out.println("");
        }
    }
    // RECORRIDOS

    // Búsqueda primero en profundidad
    public static void DFS(int u){
        System.out.print(u+" ");
        visitado[u] = true;
        for(int v = 0;v<Matrix_ady_no.length;v++){
            if(Matrix_ady_no[u][v] == 1){
                if(!visitado[v])
                    DFS(v);
            }
        }
    }
    // Primero en anchura
    public static void BFS(int i){
        Queue<Integer> cola = new LinkedList<Integer>();
        visitado[i] = true;
        cola.add(i);
        int temp;
        while(!cola.isEmpty()){
            temp = cola.remove();
            System.out.print(temp+" ");
            for(int v = 0;v<Matrix_ady_no.length;v++){
                if(Matrix_ady_no[temp][v] == 1){
                    if(!visitado[v]){
                        visitado[v] = true;
                        cola.add(v);
                    }
                        
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        for(int i = 0; i < Matrix_ady_no.length;i++)
            visitado[i] = false;
        System.out.println("Resultado de algoritmo DFS");
        DFS(0);
        for(int i = 0; i < Matrix_ady_no.length;i++)
            visitado[i] = false;
        System.out.println("\nResultado de algoritmo BFS");
        BFS(0);
        System.out.println("\nLlenando lista....");
        llenarLista();
        System.out.println("La lista es:");
        mostrarLista();
    }
}