const formulario = document.getElementById("form");

async function obterFormulario(event) {
    event.preventDefault();

    let form = new FormData(formulario)
    let campos_iterator = form.entries()
    let campos = Object.fromEntries(campos_iterator)
    let campos_json = JSON.stringify(campos)
    let campos_obj = JSON.parse(campos_json)
    let status_code = 0

    try {
        resposta = await fetch("/clientes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: campos_json
        });

        status_code = resposta.status

        const dados = await resposta.json();
        exibirNotificacao("Cliente cadastrado com sucesso!", "200", "sucesso");
        formulario.reset();
    } catch(e) {
        console.log(resposta_json)
        if (e instanceof Error){
            exibirNotificacao(`${e.name} ${e.message}`, `${status_code}`, "error");
        }
    }
}

if (formulario) {
    formulario.addEventListener("submit", obterFormulario);
}