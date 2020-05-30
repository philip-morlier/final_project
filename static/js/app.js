
// initialize base dashboard with all teams
    
    var divElement = document.getElementById('viz1590530184157');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='1100px';} 
        else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='1100px';} 
        else { vizElement.style.width='100%';vizElement.style.height='977px';}   
                      
    var scriptElement = document.createElement('script');                    
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
    vizElement.parentNode.insertBefore(scriptElement, vizElement);

// Create inputs for home and away selections
   
function initViz() {
    // var containerDiv = document.getElementById("tableauViz"),
    // url = "https://public.tableau.com/views/Project_3_NFL/TeamDashboard2?:retry=yes&:display_count=y&:origin=viz_share_link",

    // options = {
    //     disableUrlActionsPopups: true,
	//  hideTabs: true,
	//  onFirstInteractive: function () {
	//  viz.addEventListener(tableau.TableauEventName.URL_ACTION, urlActionEventHandler);
	//  console.log("Run this code when the viz has finished loading.");
	// },
    // };
    viz = new tableau.Viz("tableauPlaceholder", "https://public.tableau.com/javascripts/api/viz_v1.js", options);
        // Create a viz object and embed it in the container div.

    function urlActionEventHandler(event) {
        // Provide an event handler for the URL action to add a new feature to the dashboard.
        console.log("URL: ", event.getUrl());
        console.log("Target: ", event.getTarget());
    }
};

       
