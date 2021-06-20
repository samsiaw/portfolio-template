/**** Custom Defined Event Handlers ****/

/**
 * Animation to change text in an element after a set amount of time
 * 
 * Caller would typically use this function with the window.setInterval function
 * 
 * @param {Element} el - Element whose innerHTML is changed every `time` milliseconds
 * @param {Array<String>} textList - Array of strings to display at `time` ms intervals
 * @param {number} t - Time in milliseconds showing amount of time 
 * @return {void}
 * 
 * Note: 
 *  Function does no type-checking. It's advisable to keep the parameter types as 
 * enlisted above to prevent errors.
 */
 function loopText (el, textList, t) {
    if (el) {

        var wordIndex = this.wordIndex || 0; // Which phrase are we currently on

        var currIndex = this.currIndex || 0;
        var deleting = this.deleting || false;

        var currWord = textList[wordIndex]; // Word on display
        
        
        if (el.innerHTML.length == 0 || el.innerHTML.length == currWord.length) { // Done with showing/ deleting word
                
            deleting = !deleting;
            // Reset indices for current word
            if (el.innerHTML.length == 0) { // If we just displayed a word, we clear it before moving to next
                wordIndex = (wordIndex+1) % textList.length;
            }
            currWord = textList[wordIndex];

            if (deleting) {
                currIndex = currWord.length;
            } else {
                currIndex = 0;
            }
        }

        if ((el.innerHTML.length == currWord.length) && !this.longWaitHandled) {
            this.longWaitHandled = true; // Set so that we're not caught in the if condition above.
            //console.log("3 seconds wait");
            setTimeout(()=>loopText(el, textList, t), 3000);

        } else {
            currWord = textList[wordIndex];
            let nextText;
            if (deleting) {
                nextText = currWord.substring(0, --currIndex);
            
            } else {
                nextText = currWord.substring(0, ++currIndex);
               
            }
            el.innerHTML = nextText;
        
            this.currIndex = currIndex;
            this.deleting = deleting;
            this.wordIndex = wordIndex;

            setTimeout(()=>loopText(el, textList, t) , t); // Wait for t s before updating display
            this.longWaitHandled = false;
        }

    }
}

/**
 * Enables / Disables Prev and Next buttons depending on whether 
 * a valid "Next" or "Prev" project exists (by id)
 */
function handleNavButton() {
    // Determine if current page is a single project page
    var el = document.getElementById("project-id");

    if (el) { // Page is a single-project info page
        
        var next = document.getElementById("next");
        var prev = document.getElementById("prev");

        // Initially disabled
        next.disabled = true; 
        prev.disabled = true;

        var numString = el.value.trim();
        if (numString > "1") { //disable prev button if we're on first project, else enable

            prev.disabled = false;
        } else {
            prev.onclick = ""; // clear onclick function
        }

        var num = parseInt(numString);
        var nextUrl = getRawURL()+"/projects/"+(num+1);

        fetch(nextUrl)
        .then((response) => {
            if (response.ok) {

                    next.disabled = false;
            } else {

                next.onclick = "";
            }
        }).then(() => {

            if (!next.disabled) {

                next.onclick = () => {
                    window.location.href = nextUrl;
                }
            }     
            if (!prev.disabled) {
                var prevUrl = getRawURL()+"/projects/"+(num-1);
            
                prev.onclick = () => { 
                    window.location.href = prevUrl;
                }
            }
        });
        
    }
}


/**
 * Adds or Removes an event listener to or from all elements in the document or in a specified element (customElement)
 * tagged with the provided class (className)
 * 
 * @param {string} className - a string of the class
 * @param {string} eventName - string representing name of the event to add to the class
 * @param {Function} eventHandler - Function handler for event `eventName`
 * @param {boolean} remove - Boolean to decide adding or removing event listener
 * @param {DOMElement} customElement - Element in which to find other child elements with the specified className
 * @return {void} 
 * 
 */
function addOrRemoveListenerByClass (className, eventName, eventHandler, remove, customElement = undefined) {
    var el_list; // Elements list/ collection
    if (customElement) {
        el_list = customElement.getElementsByClassName(className);
    }
    else {
        el_list = document.getElementsByClassName(className); 
    }

    var index = 0;
    while (el_list && el_list[index]) {
        var el = el_list[index++];
        if (el) {
            if (!remove) {
                el.addEventListener(eventName, eventHandler); 
            } else {
                el.removeEventListener(eventName, eventHandler); 
            }
        }      
    }
}


/**
 * Removes an event listener from all elements in the document or 
 * in a specified element (customElement) tagged with the provided class (className)
 * 
 * @param {string} className - a string of the class
 * @param {string} eventName - string representing name of the event to add to the class
 * @param {Function} eventHandler - Function handler for event `eventName`
 * @param {DOMElement} customElement - Element in which to find other child elements with the specified className
 * @return {void} 
 * 
 */
function removeListenerByClass (className, eventName, eventHandler, customElement = undefined) {
    addOrRemoveListenerByClass(className, eventName, eventHandler, true, customElement);
}


/**
 * Removes an event listener from all elements in the document or 
 * in a specified element (customElement) tagged with the provided class (className)
 * 
 * @param {string} className - a string of the class
 * @param {string} eventName - string representing name of the event to add to the class
 * @param {Function} eventHandler - Function handler for event `eventName`
 * @param {DOMElement} customElement - Element in which to find other child elements with the specified className
 * @return {void} 
 * 
 */
function addListenerByClass (className, eventName, eventHandler, customElement = undefined) {
    addOrRemoveListenerByClass(className, eventName, eventHandler, false, customElement);
}


/**
 * Add Or Remove a listener to/from a specified ID's element
 * 
 * @param {string} IDName - string for ID
 * @param {string} eventName - name of event to which a listener is added/removed
 * @param {Function} eventHandler - function for handling event
 * @param {boolean} remove - Boolean to decide adding or removing event listener
 * @return {void} 
 */
function addOrRemoveListenerById (IDName, eventName, eventHandler, remove) {
    var el = document.getElementById(IDName);
    if (el) {
        if (!remove) {
            el.addEventListener(eventName, eventHandler);
        } else {
            el.removeEventListener(eventName, eventHandler);
        }
    }
    else console.log(IDName + " is not a defined ID");
}


/**
 * Add a listener to a specified ID's element
 * 
 * @param {string} IDName - string for ID
 * @param {string} eventName - name of event to which a listener is added
 * @param {Function} eventHandler - function for handling event
 * @return {void} 
 */
function addListenerById (IDName, eventName, eventHandler) {
    addOrRemoveListenerById(IDName, eventName, eventHandler, false)
}


/**
 * Remove a listener from a specified ID's element
 * 
 * @param {string} IDName - string for ID
 * @param {string} eventName - name of event to which a listener is removed
 * @param {Function} eventHandler - function for handling event
 * @return {void} 
 */
function addListenerById (IDName, eventName, eventHandler) {
    addOrRemoveListenerById(IDName, eventName, eventHandler, true)
}


/** 
 * Removes all child elements of the current element from the DOM
 * 
 * @param {Element} el - Element whose children would be deleted
 */
function removeChildren(el) {
    //el.innerHTML = '';
    while (el.lastChild) {
        el.removeChild(el.lastChild);
    }
}


/**
 * Converts all programming language text to images
 */
function langToImg() {
    var langs = document.getElementsByClassName('tool');

    var index = 0;
    while (langs && langs[index]) { // Loop through all programming language texts
        var img = langs[index++];

        var langName = img.alt.trim();
        img.src = getStaticPath() + "/images/" + langName +".png";
    }
}
/**
 * Returns a string of the current window url containing only
 * the protocol, hostname, (and port number if it exists)
 * 
 * @return {string} 
 */
function getRawURL() {
    var location = window.location;
    var url = location.protocol+'//'+
              location.hostname+
              (location.port ? ':'+location.port: '');
    return url;
}

/**
 * Returns the string path for static files
 * 
 * @return {string} 
 */
function getStaticPath(){
    return document.getElementById('static').value;
}

/**
 * Checks if element contains a specified class
 * 
 * @param {Element} el
 * @param {string} el_class
 * 
 * @reaturn {Boolean} 
 */
function containsClass(el, el_class) {
   return el.classList.contains(el_class)
}


/**
 * Register all event listeners
 * 
 * @param {Event} event - event to attach current function to (used for the "DOMContentLoaded" event)
 */
 function registerEventHandlers (event) {

   //addListenerByClass('navbar-item', 'click', handleNav);

    langToImg(); // Convert tools/language txts to images

    // Next and Prev Button logic for single project display
    handleNavButton();
}


/**
 * Deregister all event listeners
 * 
 * @param {Event} event - event to attach this function to (used for the "unload" event)
 */
function deregisterEventHandlers (event) {
      
}


// Add Listeners to the document's main DOM
document.addEventListener('DOMContentLoaded', registerEventHandlers);
document.addEventListener('unload', deregisterEventHandlers);

/**
 * Force CSS reload from script
 */
// function cssReload() {
//     //console.log("cssReload: attempting");
//     var src = document.getElementById('css-src');
//     var allLinks = document.getElementsByTagName('link');
//     for (var link in allLinks) {
//         if (allLinks[link].rel === "stylesheet") {
//             //console.log("cssReload: found stylesheet");
//             allLinks[link].href = src.value+"?t="+ Date.now();
//         }
//     }
// }
