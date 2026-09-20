console.log("initialized")
const a = document.querySelector(".down")
const sub = document.querySelector(".sub")
sub.addEventListener('submit', async function(event){
    event.preventDefault();
    alert("Uploading Please wait for 2-3 Minutes");
    const formdata = new FormData(sub)
    const response  = await fetch('/upload', {
        method: 'POST',
        body: formdata, 
    })
    if (response.ok){
     console.log("MIssion sucessful")
    a.style.display = "grid";
    a.href = "static/compressed.jpg?t=" + Date.now();}
    else {
        console.log("failed")
        alert("Please add a File")
    }
})
