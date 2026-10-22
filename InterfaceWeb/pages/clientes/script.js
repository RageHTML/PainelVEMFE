const formulario = document.getElementById("form");

async function obterFormulario(event) {
    event.preventDefault();

    let form = new FormData(formulario)
    let campos_iterator = form.entries()
    let campos = Object.fromEntries(campos_iterator)
    let campos_json = JSON.stringify(campos)
    let campos_obj = JSON.parse(campos_json)
    let status_code = 0

    resposta = await fetch("/clientes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: campos_json
    });

    const dados = await resposta.json();
    status_code = resposta.status
    console.log(dados)

    if (resposta.ok == false){
        exibirNotificacao(`${dados.detail}`, `${status_code}`, "error");
    } else {
        exibirNotificacao("Cliente cadastrado com sucesso!", "200", "sucesso");
        formulario.reset();
    }

}

if (formulario) {
    formulario.addEventListener("submit", obterFormulario);
}