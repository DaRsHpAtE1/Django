function check() {
    let nu = document.getElementById("nu")
    let ans = document.getElementById("ans")
    if (nu.value == "") {
        alert("Number Cannot Be Empty")
        nu.focus()
        ans.innerHTML = ""
        return false
    }
    else {
        return true
    }
}
