// Fills the product box when an example is clicked.
// This does not look up a price. It only helps you try the form.

const productInput = document.querySelector("#product");
const examples = document.querySelector(".examples ul");

if (productInput && examples) {
    const names = ["Rice 5kg", "Milk 1 litre", "Shampoo 650ml", "Laptop", "Mobile phone"];
    examples.innerHTML = "";

    names.forEach((name) => {
        const item = document.createElement("li");
        const button = document.createElement("button");
        button.type = "button";
        button.className = "chip";
        button.textContent = name;
        button.addEventListener("click", () => {
            productInput.value = name;
            productInput.focus();
        });
        item.appendChild(button);
        examples.appendChild(item);
    });
}
