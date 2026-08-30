const inputNome = document.getElementById("nome_completo");
const inputIdOculto = document.getElementById("cliente_id");
const dataList = document.getElementById("lista_clientes");
const formulario = document.getElementById("form");
let clientesEncontrados = []; 

inputNome.addEventListener("input", async (event) => {
    const texto = event.target.value;

    if (texto.length >= 2) {
        const resposta = await fetch(`/produtos/clientes?nome=${texto}`);
        clientesEncontrados = await resposta.json();

        dataList.innerHTML = "";

        clientesEncontrados.forEach(cliente => {
            const option = document.createElement("option");
            option.value = `${cliente.nome_completo}`;
            dataList.appendChild(option);
        });
    }

    const clienteSelecionado = clientesEncontrados.find(
        c => `${c.nome_completo}` === texto
    );

    if (clienteSelecionado) {
        inputIdOculto.value = clienteSelecionado.id;
        console.log("ID do cliente vinculado:", clienteSelecionado.id);
    } else {
        inputIdOculto.value = ""
    }
});

async function obterFormulario(event) {
    event.preventDefault(); 
    const nome_completo = document.getElementById("nome_completo").value;
    const cliente_id = document.getElementById("cliente_id").value;
    const descricao = document.getElementById("descricao").value;
    const valor = document.getElementById("valor").value;
    const forma_pagamento = document.getElementById("forma_pagamento").value;
    const status = document.getElementById("status").value;
    
    
    const dadosProdutos = {
        nome_completo: nome_completo,
        cliente_id: cliente_id,
        descricao: descricao,
        valor: valor,
        forma_pagamento: forma_pagamento,
        status: status
    }

    const resposta = await fetch("/produtos/clientes/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(dadosProdutos)
    })

    const dados = await resposta.json();

    console.log("Resposta do FastAPI:", dados);
}


formulario.addEventListener("submit", obterFormulario);