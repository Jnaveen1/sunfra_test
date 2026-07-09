async function saveData() {


    const name = document.getElementById("name").value;

    const email = document.getElementById("email").value;



    const response = await fetch("/save", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },


        body: JSON.stringify({

            name: name,

            email: email

        })

    });



    const result = await response.json();


    console.log(result);


    alert("Saved successfully!");

}