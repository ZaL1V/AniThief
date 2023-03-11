const theme = document.getElementById("theme");

theme.addEventListener("change", function () {
    if (this.value === "auto") {
        document.documentElement.removeAttribute("data-theme");
        localStorage.removeItem("data-theme");
    } else {
        document.documentElement.setAttribute("data-theme", this.value);
        localStorage.setItem("data-theme", this.value);
    }
});

window.addEventListener("load", function () {
    const storedTheme = localStorage.getItem("data-theme");

    if (storedTheme) {
        theme.value = storedTheme;
        document.documentElement.setAttribute("data-theme", storedTheme);
    }
});