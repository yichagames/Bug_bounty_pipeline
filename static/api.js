document.addEventListener("click", async e => {
    const btn = e.target.closest('.api-btn')
    if (!btn) return
    await api(btn.dataset.path)
})

async function api(path, method="GET", data = null){
    const api_path = `/api/${path}`
    const option = {
        method,
        headers: {}
    }
    if (data) {
        option.headers["Content-Type"] = "application/json"
        option.body = JSON.stringify(data)
    }
    const res = await fetch(api_path, option)
    let text = await res.json()
    await console.log(text)
    return text
}

document.addEventListener("submit", async e => {
    const form = e.target.closest(".api_forms")
    if(!form) return
    e.preventDefault()

    const data = Object.fromEntries(new FormData(form))
    const action = form.dataset.action
    const method = (form.method || "POST").toUpperCase();
    
    await fetch(`/api/${action}`, {
        method: method,
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(data)
    })
    location.reload()
})