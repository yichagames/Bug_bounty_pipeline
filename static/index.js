document.addEventListener('DOMContentLoaded', async () => {
    const home = document.getElementById("home")
    const dashboard = document.getElementById("dashboard")
    const projects = document.getElementById("projects")
    const settings = document.getElementById("settings")

    const dim = document.getElementById("dim")

    const projects_popup = document.getElementById("projects_popup")
    const Delete_dropdown = document.getElementById("Delete_project_dropdown")
    var all_projects_result = await api("Fetch_all_projects")
    var all_projects = all_projects_result.result

    all_projects.forEach(e => {
        const options = document.createElement("option")
        options.value = e
        options.textContent = e
        Delete_dropdown.appendChild(options)
    });

    const settings_popup = document.getElementById("settings_popup")
    
    settings.addEventListener("click", (e) => {
        settings_popup.classList.add("opened")
        projects_popup.classList.remove("opened")
    })
    projects.addEventListener("click",(e) => {
        projects_popup.classList.add("opened")
        settings_popup.classList.remove("opened")
    })
    dim.addEventListener("click", () => {
        settings_popup.classList.remove("opened")
        projects_popup.classList.remove("opened")
    })
})