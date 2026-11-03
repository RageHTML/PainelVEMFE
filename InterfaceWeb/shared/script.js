document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-btn');

    toggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
    });
});


let pop_ativo = false;
function exibirNotificacao(mensagem, codigo, tipo) {
    if (pop_ativo == true) return;

    const container = document.getElementById("notificacao-container");
    if (!container) return;

    const notificacao = document.createElement("div");
    notificacao.className = `notificacao ${tipo}`;
    notificacao.textContent = `${codigo} | ${mensagem} `;
    container.appendChild(notificacao);
    pop_ativo = true;

    setTimeout(() => {
        pop_ativo = false;
        notificacao.classList.add("esconder");
        setTimeout(() => {
            notificacao.remove();
        }, 400); 
    }, 5000);
}