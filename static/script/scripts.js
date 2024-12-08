document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("workoutForm");
    const workoutTableBody = document.getElementById("dash-apps-list");

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

            if (!response.ok) {
                throw new Error("Failed to fetch workout data");
            }

            // Parse the API response
            const workoutData = await response.json();

            // Clear previous table data
            workoutTableBody.innerHTML = "";

            // Add the workout data to the table
            workoutData.forEach((workout) => {
                const { name, sets, reps, instructions, images } = workout;

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
                    stepsRows += `<div class="row step-row">${index + 1}. ${step}</div>`
                });    

                const instructionRow = document.createElement("tr");
                instructionRow.innerHTML = `
                    <td class="col">
                        ${stepsRows}
                    </td>
                    <td class="col">${images[0] ? `<img src="${appendImageUrl(images[0])}" alt="Workout Image 1" style="width:100px;">` : ""}</td>
                    <td class="col">${images[1] ? `<img src="${appendImageUrl(images[1])}" alt="Workout Image 2" style="width:100px;">` : ""}</td>
                `;
                workoutTableBody.appendChild(instructionRow);
                
            });
        } catch (error) {
            console.error("Error:", error.message);
            alert("There was an issue generating your workout. Please try again.");
        }
    });
});


function appendImageUrl(imageName){
    return `https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/${imageName}`;
}