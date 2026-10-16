const formulario = document.getElementById("form");

async function obterFormulario(event) {
    event.preventDefault();

    const dadosClientes = {
        nome_completo: document.getElementById("nome_completo").value,
        nome_mae: document.getElementById("nome_mae").value,
        cpf: document.getElementById("cpf").value,
        data_nascimento: document.getElementById("data_nascimento").value || null,
        endereco: document.getElementById("endereco").value
    };

    try {
        const resposta = await fetch("/clientes/registrar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dadosClientes)
        });

        if (!resposta.ok) {
            const erroJson = await resposta.json().catch(() => ({ menssagem: "Falha ao processar o json", codigo: "200",  tipo: "error"}));
            exibirNotificacao(erroJson.menssagem, erroJson.codigo, errorJson.tipo);
            return;
        }

        const dados = await resposta.json();
        exibirNotificacao("Cliente cadastrado com sucesso!", "200", "sucesso");
        formulario.reset();

    } catch (erro) {
        exibirNotificacao("Erro de conexão com o servidor", "400", "error");
    }
}

if (formulario) {
    formulario.addEventListener("submit", obterFormulario);
}