const honeytokenButtons = document.querySelectorAll(".honeytoken-btn");

honeytokenButtons.forEach(button => {

    button.addEventListener("click", function () {

        const resourceName = this.dataset.resource;

        fetch("/honeytoken-access", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resource: resourceName
            })
        })
        .then(response => response.json())
        .then(data => {
            alert("Security Alert: " + data.message);
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Unable to contact the security server.");
        });

    });

});