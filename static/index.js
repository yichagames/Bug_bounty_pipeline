document.addEventListener('DOMContentLoaded', async () => {
    // aside
    const home = document.getElementById("home")
    const dashboard = document.getElementById("dashboard")
    const projects = document.getElementById("projects")
    const settings = document.getElementById("settings")


    // popup windows
    const dim = document.getElementById("dim")

    const projects_popup = document.getElementById("projects_popup")
    const all_projects_dropdowns = [document.getElementById("Delete_project_dropdown"), document.getElementById("Change_project_dropdown")]
    var all_projects = await api("Fetch_all_projects")
    var all_projects_result = Object.keys(all_projects.result)

    all_projects_result.forEach(e => {
        all_projects_dropdowns.forEach(r => {
            const options = document.createElement("option")
            options.value = e
            options.textContent = e
            r.appendChild(options)
        })
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


    // main
    const info_domain = document.getElementById("info_domain")
    const Current_project = await api("Current_project")
    info_domain.innerText = Current_project.result
})