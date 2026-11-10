const campo_busca = document.getElementById("busca");
const lista_clientes = document.getElementById("lista_clientes");
const formulario = document.getElementById("form");
let clienteEncontrado = null;

if (campo_busca) {
    campo_busca.addEventListener("input", async (event) => {
        const texto = event.target.value.trim();

        if (texto.length >= 1) {
            try {
                const resposta = await fetch(`/clientes/buscar`,{
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ nome: texto })
                });

                const dados = await resposta.json();

                if (dados != null) {
                    clienteEncontrado = dados;
                } else {
                    clienteEncontrado = null;
                }

                if (clienteEncontrado != null) {
                    lista_clientes.innerHTML = "";
                    const option = document.createElement("option");
                    option.value = clienteEncontrado;
                    lista_clientes.appendChild(option);
                }
            } catch (erro) {
                clientesEncontrados = null;
                exibirNotificacao('Erro de conexão com o servidor', '400', "error");
            }
        } else {
            clientesEncontrados = null;
            if (lista_clientes) lista_clientes.innerHTML = "";
        }
    });
}


if (formulario) {
    formulario.addEventListener("submit", async (event) => {
        event.preventDefault();

        let form = new FormData(formulario)
        let campos_iterator = form.entries()
        let campos = Object.fromEntries(campos_iterator)
        let campos_json = JSON.stringify(campos)
        let campos_obj = JSON.parse(campos_json)
        let status_code = 0

       

        resposta = await fetch("/produtos/novo", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: campos_json
        });

        console.log(campos_json)

        const dados = await resposta.json();
        status_code = resposta.status

        if (resposta.ok == false){
            exibirNotificacao(`${dados.detail}`, `${status_code}`, "error");
        } else {
            exibirNotificacao("Cliente cadastrado com sucesso!", "200", "sucesso");
            formulario.reset();
        }
    });
}
