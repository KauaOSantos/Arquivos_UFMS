public class ContaCorrente {
    float juros = 0.01f;
    float saldo;
    float limiteChequeEspecial = -200;
    String primeiroNome;
    String sobrenome;
    long numeroConta;

    public ContaCorrente(String primeiroNome, String sobrenome, long numeroConta) {
        this.primeiroNome = primeiroNome;
        this.sobrenome = sobrenome;
        this.numeroConta = numeroConta;
        this.saldo = 0;
    }

    public void deposito(float valor) {
        if (valor > 0) {
            saldo += valor;
        }
    }

    public void saque(float valor) {
        if (saldo - valor >= limiteChequeEspecial) {
            saldo -= valor;
        } else {
            System.out.println("Limite insuficiente!");
        }
    }

    public void rendimento() {
        if (saldo > 0) {
            saldo += saldo * juros;
        }
    }

    public void exibirSaldo() {
        System.out.printf("Saldo: R$ %.2f%n", saldo);
    }

    public String getNome() {
        return primeiroNome + " " + sobrenome;
    }

    // Método para obter o número da conta
    public long getNumero() {
        return numeroConta;
    }

    // Método main para testar a classe
    public static void main(String[] args) {
        ContaCorrente conta = new ContaCorrente("Matheus", "Silva", 123456789);

        conta.deposito(100);
        conta.exibirSaldo();

        conta.saque(125);
        conta.exibirSaldo();

        conta.rendimento();
        conta.exibirSaldo();
    }
}
