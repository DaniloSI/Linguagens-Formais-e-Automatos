package dominio;


public class Politico {
    private String  nome;

    private boolean honesto;

    public Politico() {

    }

    public Politico(String nome, boolean honesto) {
        super();
        this.nome = nome;
        this.honesto = honesto;
    }

    public boolean isHonesto() {
        return honesto;
    }

    public void setHonesto(boolean honesto) {
        this.honesto = honesto;
    }

    public String getNome() {
        return nome;
    }
}
