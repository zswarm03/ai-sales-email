document.getElementById("emailForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let product = document.getElementById("product").value;
    let behavior = document.getElementById("behavior").value;

    let response = await fetch("/generate-email", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, product: product, behavior: behavior })
    });

    let data = await response.json();
    document.getElementById("generatedEmail").innerText = data.email;
});

