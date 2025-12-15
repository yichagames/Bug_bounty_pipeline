document.addEventListener("click", async function(e){
    const btn = e.target.closest('.api-btn')
    if (!btn) return
    await api(btn.dataset.path)
})

async function api(path, method="GET", data = null){
    api_path = "api/" + path
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
    console.log(text)
}