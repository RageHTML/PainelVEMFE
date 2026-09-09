const inputNome = document.getElementById("nome_completo");
const inputIdOculto = document.getElementById("cliente_id");
const dataList = document.getElementById("lista_clientes");
const formulario = document.getElementById("form");
let clientesEncontrados = [];

function exibirToast(mensagem, tipo = "sucesso", tempo = 3000) {
    let container = document.getElementById("toast-container");
    if (!container) {
        container = document.createElement("div");
        container.id = "toast-container";
        document.body.appendChild(container);
    }

    const toast = document.createElement("div");
    toast.className = `toast ${tipo}`;
    toast.textContent = mensagem;

    container.appendChild(toast);

    setTimeout(() => {
        toast.classList.add("esconder");
        setTimeout(() => {
            toast.remove();
        }, 400);
    }, tempo);
}

if (inputNome) {
    inputNome.addEventListener("input", async (event) => {
        const texto = event.target.value.trim();

        if (texto.length >= 2) {
            try {
                const resposta = await fetch(`/produtos/clientes?nome=${encodeURIComponent(texto)}`);
                const dados = await resposta.json();

                if (Array.isArray(dados)) {
                    clientesEncontrados = dados;
                } else if (dados && Array.isArray(dados.clientes)) {
                    clientesEncontrados = dados.clientes;
                } else {
                    clientesEncontrados = [];
                }

                if (dataList) {
                    dataList.innerHTML = "";
                    clientesEncontrados.forEach(cliente => {
                        const option = document.createElement("option");
                        option.value = cliente.nome_completo;
                        dataList.appendChild(option);
                    });
                }
            } catch (erro) {
                clientesEncontrados = [];
            }
        } else {
            clientesEncontrados = [];
            if (dataList) dataList.innerHTML = "";
        }

        const clienteSelecionado = clientesEncontrados.find(c => c.nome_completo === texto);

        if (clienteSelecionado) {
            inputIdOculto.value = clienteSelecionado.id;
        } else {
            inputIdOculto.value = "";
        }
    });
}

async function obterFormulario(event) {
    event.preventDefault();

    const rawId = inputIdOculto ? inputIdOculto.value : null;
    const rawValor = document.getElementById("valor").value;

    const dadosProdutos = {
        nome_completo: document.getElementById("nome_completo").value,
        cliente_id: rawId ? parseInt(rawId, 10) : null,
        descricao: document.getElementById("descricao").value,
        valor: parseFloat(rawValor) || 0.0,
        forma_pagamento: document.getElementById("forma_pagamento").value
    };

    try {
        const resposta = await fetch("/produtos/clientes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dadosProdutos)
        });

        if (!resposta.ok) {
            const erroJson = await resposta.json().catch(() => ({ detail: "Erro ao cadastrar produto." }));
            exibirToast(erroJson.detail || "Erro ao cadastrar produto", "erro");
            return;
        }

        exibirToast("Produto cadastrado com sucesso!", "sucesso");
        formulario.reset();
        if (inputIdOculto) inputIdOculto.value = "";
        if (dataList) dataList.innerHTML = "";

    } catch (erro) {
        exibirToast("Erro de conexão com o servidor", "erro");
    }
}

if (formulario) {
    formulario.addEventListener("submit", obterFormulario);
}