function check() {
    let num = document.getElementById("num")
    let ans = document.getAnimations("ans")
    if ((num.value < 0) || (num.value == "")) {
        alert("Invalid")
        num.value = ""
        num.focus()
        ans.innerHTML
        return false
    }
    else {
        return true
    }

}