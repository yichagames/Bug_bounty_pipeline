document.addEventListener('DOMContentLoaded', () => {
    const home = document.getElementById("home")
    const dashboard = document.getElementById("dashboard")
    const projects = document.getElementById("projects")
    const settings = document.getElementById("settings")

    const projects_popup = document.getElementById("projects_popup")
    const settings_popup = document.getElementById("settings_popup")
    const dim = document.getElementById("dim")

    for (let i = 0; i < document.forms.length; i++) {
        document.forms[i].addEventListener("keydown", function(e){
            if (e.key != "Enter") return
            this.submit()
        })
    }
    
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