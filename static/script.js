function autoResize(textarea) {
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
}

document.addEventListener("DOMContentLoaded", function() {
    const areas = document.querySelectorAll("textarea");
    areas.forEach(area => {
        autoResize(area);
        area.addEventListener("input", () => autoResize(area));
    });
});
