package herencia_multiple_java;

import java.util.Scanner;

/**
 *
 * @author Javier Sanchez
 */
public class main{

    public static void main(String[] args){
        String bebida;
        System.out.println("Ingrese que bebida desea servir en el vaso: ");
        Scanner s = new Scanner(System.in);
        bebida = s.nextLine();
        VasoComun vaso = new VasoComun();
        vaso.servir(bebida);
    }

}

