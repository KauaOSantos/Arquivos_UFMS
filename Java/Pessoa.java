public class Pessoa {
    String nome;
    int idade;

    public void exibirInformacoes() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
    }

    public void fazerAniversario() {
        idade++;
        System.out.println(nome + " fez aniversário e agora tem " + idade + " anos.");
    }
}


public class TestePessoa {
    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa();
        
        pessoa.nome = "Ana";
        pessoa.idade = 30;

        pessoa.exibirInformacoes();
        pessoa.fazerAniversario();
        pessoa.exibirInformacoes();
    }
}
