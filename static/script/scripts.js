document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("workoutForm");
    const workoutTableBody = document.getElementById("dash-apps-list");
    const workoutDescription = document.getElementById("workout-description"); // Element to display workout description


    

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Gather form data
        const formData = new FormData(form);
        const formObject = {};
        formData.forEach((value, key) => {
            if (formObject[key]) {
                // If key already exists (e.g., checkboxes), convert to array
                formObject[key] = [].concat(formObject[key], value);
            } else {
                formObject[key] = value;
            }
        });

        try {
            // Send the form data to the API
            const response = await fetch("/api/generate-workout", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formObject)
            });

            // console.log(JSON.stringify(formObject));

            if (!response.ok) {
                throw new Error("Failed to fetch workout data" + response.status);
            }

            // Parse the API response
            const data = await response.json();
            
            // console.log("API Response:", data);

            if (!data.WorkoutPlanDescription || !data.WorkoutJson) {
                console.error("Invalid API response:", data);
                alert("Received incomplete data from the server.");
                return;
            }

            const WorkoutPlanDescription = data.WorkoutPlanDescription;
            const WorkoutJson = data.WorkoutJson;

            // console.log("WorkoutPlanDescription: ", WorkoutPlanDescription);
            // console.log("WorkoutJson: ", WorkoutJson);

            if (!Array.isArray(WorkoutJson)) {
                console.error("WorkoutJson is not an array:", WorkoutJson);
                alert("Invalid workout data received from the server.");
                return;
            }
            
            // Update workout description
            workoutDescription.textContent = WorkoutPlanDescription;

            // Clear previous table data
            workoutTableBody.innerHTML = "";

            // Add the workout data to the table
            WorkoutJson.forEach((workout) => {
                const { name, sets, reps, instructions = [], images = [] } = workout;

                // Create a row for the workout details
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td><strong>${name}</strong></td>
                    <td>${sets}</td>
                    <td>${reps}</td>
                `;
                workoutTableBody.appendChild(row);

                // Add instructions and images
                let stepsRows = '';
                instructions.forEach((step, index) => {
                    stepsRows += `<div class="row step-row" style="padding: 5px;">${index + 1}. ${step}</div>`;
                });

                const instructionRow = document.createElement("tr");
                instructionRow.innerHTML = `
                    <td class="col">${stepsRows}</td>
                    <td class="col">${images[0] ? `<img class="workout-image" src="${appendImageUrl(images[0])}" alt="Workout Image 1" style="width:100px; cursor:pointer;">` : ""}</td>
                    <td class="col">${images[1] ? `<img class="workout-image" src="${appendImageUrl(images[1])}" alt="Workout Image 2" style="width:100px; cursor:pointer;">` : ""}</td>
                `;
                workoutTableBody.appendChild(instructionRow);
            });

            

            setupModal();
        } catch (error) {
            console.error("Error:", error.message);
            alert("There was an issue generating your workout. Please try again.");
        }
    });
});

function appendImageUrl(imageName) {
    return `https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/${imageName}`;
}

function setupModal() {    
    const imageModal = document.createElement("div");
    imageModal.id = "imageModal";
    imageModal.style.cssText = `
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        justify-content: center;
        align-items: center;
        z-index: 1000;
    `;

    const modalImage = document.createElement("img");
    modalImage.id = "modalImage";
    modalImage.style.cssText = `
        max-width: 90%;
        max-height: 90%;
    `;
    imageModal.appendChild(modalImage);

    const closeModal = document.createElement("span");
    closeModal.id = "closeModal";
    closeModal.textContent = "×";
    closeModal.style.cssText = `
        position: absolute;
        top: 10px;
        right: 20px;
        color: white;
        font-size: 2rem;
        cursor: pointer;
    `;
    imageModal.appendChild(closeModal);

    document.body.appendChild(imageModal);
    // Close the modal when the close button is clicked
    closeModal.addEventListener("click", function () {
        imageModal.style.display = "none";
        modalImage.src = "";
    });

    // Close the modal when clicking outside the image
    imageModal.addEventListener("click", function (event) {
        if (event.target === imageModal) {
            imageModal.style.display = "none";
            modalImage.src = "";
        }
    });

    // Add click event to images for the modal
    document.querySelectorAll(".workout-image").forEach((img) => {
        img.addEventListener("click", function () {
            modalImage.src = this.src; // Set the clicked image as the modal's image
            imageModal.style.display = "flex"; // Show the modal
        });
    });
}