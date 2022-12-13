// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Set the URL and method for the request
xhr.open("POST", "https://example.com/upload");

// Set the request header to specify that it is an XML file
xhr.setRequestHeader("Content-Type", "text/xml");

// Create a FormData object to hold the XML file
var formData = new FormData();

// Add the XML file to the FormData object
formData.append("file", xmlFile);

// Send the request
xhr.send(formData);
