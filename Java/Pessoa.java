public class Pessoa {
    // Atributos
    String nome;
    int idade;

    // Método para exibir informações da pessoa
    public void exibirInformacoes() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
    }

    // Método para fazer aniversário (incrementa a idade)
    public void fazerAniversario() {
        idade++;
        System.out.println(nome + " fez aniversário e agora tem " + idade + " anos.");
    }
}


public class TestePessoa {
    public static void main(String[] args) {
        // Criando um objeto da classe Pessoa
        Pessoa pessoa = new Pessoa();
        
        // Inicializando atributos
        pessoa.nome = "Ana";
        pessoa.idade = 30;

        // Chamando metodos do objeto
        pessoa.exibirInformacoes();
        pessoa.fazerAniversario();
        pessoa.exibirInformacoes();
    }
}
