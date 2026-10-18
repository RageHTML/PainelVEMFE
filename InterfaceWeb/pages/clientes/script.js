const formulario = document.getElementById("form");



async function obterFormulario(event) {
    event.preventDefault();

    let form = new FormData(formulario)
    let campos_iterator = form.entries()
    let campos = Object.fromEntries(campos_iterator)
    const campos_json = JSON.stringify(campos);
    
    try {
        const resposta = await fetch("/clientes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: campos_json
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