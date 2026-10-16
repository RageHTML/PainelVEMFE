document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-btn');

    toggleBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
    });
});

function exibirNotificacao(mensagem, codigo, tipo) {
    tempo = 3000
    const container = document.getElementById("notificacao-container");
    if (!container) return;

    const notificacao = document.createElement("div");
    notificacao.className = `notificacao ${tipo}`;
    notificacao.textContent = `${codigo} | ${mensagem} `;
    container.appendChild(notificacao);

    setTimeout(() => {
        notificacao.classList.add("esconder");
        setTimeout(() => {
            notificacao.remove();
        }, 400); 
    }, tempo);
}