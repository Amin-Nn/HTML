const button = document.getElementById("btn");
const text = document.getElementById("name");
const colors = ["red", "blue", "green", "orange", "purple", "lightblue", "yellow", "gray", "black"];
let colorIndex = 0;

function changeColor() {

    text.style.color = colors[colorIndex];
    colorIndex = (colorIndex + 1) % colors.length;

    }
button.addEventListener("click", changeColor);



const time = new Date().getHours();
if (time < 12) {
    var greetingTime = "sabahınız xeyir";
} else if (time < 18) {
    var greetingTime = "günortanız xeyir";
} else {
    var greetingTime = "axşamınız xeyir";
}
const button1 = document.getElementById("greet");
button1.addEventListener("click", function() {
    alert("Salam, " + greetingTime + "! Portfolio saytıma xoş gəlmisiniz!");
});




function hideSection() {
    const aboutSection = document.getElementById("about");
    const showButton = document.getElementById("show");

    aboutSection.style.display = "none";
    showButton.style.visibility = "visible";
}


function showSection() {
    const aboutSection = document.getElementById("about");
    const showButton = document.getElementById("show");

    aboutSection.style.display = "block";
    showButton.style.visibility = "hidden";
}


const addProjectButton = document.getElementById('add-project');
const projectList = document.getElementById('project-list');

addProjectButton.addEventListener('click', function() {
    const projectLinkInput = document.getElementById('project-link');
    const projectLink = projectLinkInput.value.trim();

    if (projectLink) {
        const projectItem = document.createElement('div');
        projectItem.className = 'project-item';

        const link = document.createElement('a');
        link.href = projectLink.startsWith('http') ? projectLink : 'https://' + projectLink;
        link.textContent = projectLink;
        link.target = '_blank';

        projectItem.appendChild(link);
        projectList.appendChild(projectItem);
        projectLinkInput.value = '';
    }
});