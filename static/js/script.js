function accessResource(resourceName) {

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

        const message = document.getElementById("access-message");

        message.style.display = "flex";

        setTimeout(() => {
            message.style.display = "none";
        }, 2500);

    })

    .catch(error => {

        console.error("Resource access error:", error);

    });
}