document.addEventListener("DOMContentLoaded", () => {
  const loginBtn = document.getElementById("loginBtn");
  const modal = document.getElementById("loginModal");
  const closeModal = document.querySelector(".close");
  const loginView = document.getElementById("loginView");
  const detailsView = document.getElementById("detailsView");
  const loginForm = document.getElementById("loginForm");
  const personalDetailsForm = document.getElementById("personalDetailsForm");
  const welcomeUser = document.getElementById("welcomeUser");
  const resultsSection = document.getElementById("resultsSection");

  let currentUsername = "";

  // Open modal
  loginBtn.addEventListener("click", () => {
    loginView.classList.remove("hidden");
    detailsView.classList.add("hidden");
    modal.classList.add("show");
  });

  // Close modal
  closeModal.addEventListener("click", () => {
    modal.classList.remove("show");
  });

  window.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.classList.remove("show");
    }
  });

  // Login form
  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    currentUsername = document.getElementById("username").value.trim();

    if (currentUsername) {
      welcomeUser.textContent = `👋 Hello, ${currentUsername}`;
      welcomeUser.classList.remove("hidden");
      loginBtn.classList.add("hidden");
      loginForm.reset();

      // Switch to details view
      loginView.classList.add("hidden");
      detailsView.classList.remove("hidden");
    }
  });

  // Personal Details form
  personalDetailsForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(personalDetailsForm);
    const userDetails = {};
    formData.forEach((value, key) => {
      userDetails[key] = value;
    });

    try {
      const [nutrition, activity, medication, mood] = await Promise.all([
		callApi("http://127.0.0.1:5000/api/nutrition", userDetails),
		callApi("http://127.0.0.1:5000/api/activity", userDetails),
		callApi("http://127.0.0.1:5000/api/medication", userDetails),
		callApi("http://127.0.0.1:5000/api/mood-tracker", userDetails)
      ]);

      document.getElementById("nutritionResult").textContent = nutrition;
      document.getElementById("activityResult").textContent = activity;
      document.getElementById("medicationResult").textContent = medication;
      document.getElementById("moodResult").textContent = mood;

      resultsSection.classList.remove("hidden");
      modal.classList.remove("show");
    } catch (error) {
      console.error("Error:", error);
      alert("Oops! Something went wrong. Please try again.");
    }
  });

  async function callApi(endpoint, data) {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error(`Error from ${endpoint}`);
    const json = await response.json();
    return json.response || JSON.stringify(json, null, 2);
  }
});