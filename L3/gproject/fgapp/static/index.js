function check() {
    let marks = document.getElementById("marks")
    let ans = document.getElementById("ans")
    if ((marks.value == "") || (marks.value > 100) || (marks.value < 0)) {
        alert("Invalid Marks")
        marks = ""
        ans.innerHTML = ""
        marks.focus()
        return false

    }
    else {
        return true
    }
}