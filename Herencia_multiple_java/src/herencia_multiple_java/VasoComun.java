package herencia_multiple_java;

public class VasoComun implements VasoAgua, VasoGaseosa, VasoCerveza{
    @Override
    public void servir(String bebida) {
        System.out.println("Aqui esta su vaso de " + bebida);
        throw new UnsupportedOperationException("Not supported yet.");
    }
}
