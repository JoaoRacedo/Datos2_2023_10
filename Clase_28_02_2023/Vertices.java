import java.util.LinkedList;
public class Vertices {
    
    int dato;
    LinkedList<Integer> adyacentes;
    public Vertices(int dato){
        this.dato = dato;
        adyacentes = new LinkedList<Integer>();
    }

    public int getDato(){
        return dato;
    }

    public LinkedList<Integer> getAdyacentes(){
        return adyacentes;
    }
}