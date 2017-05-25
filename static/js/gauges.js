//Change color of the gauge when it reaches certain percentage ranges.
function change_color(obj, newval){
    //set to green.
    var newcolor = "#48CFAD"
    
    if(newval >= 70 && newval < 90){
        //set to yellow.
        newcolor =  "#FFCE54"
    }
    else if (newval > 89){
        //set to red.
        newcolor = "#FC6E51"
    }
    //change the gauge color.
    obj.trigger(
     'configure',
      {
        "fgColor": newcolor,
        "readOnly": true
      }
    );
    //change the text color of the gauge.
    obj.css("color", newcolor)
}

//Animate the gauge given jQuery div object of the gauge, it's previous value and its new value to be set.
function animate_gauge(obj, preval, newval){
    if (preval == newval){
       return;
    }
    $({value: preval}).animate({value: newval}, {
        duration: 1000,
        easing:'swing',
        step: function() 
        {
            obj.val(this.value).trigger('change');
            change_color(obj, this.value);
        }
    });
}

//Invokes backend call to retrieve data for the gauge and then animates it to the UI.
function run_gauge(gauge_name){
    $.ajax( {url: "get" + gauge_name.charAt(0).toUpperCase() + gauge_name.slice(1) + "Usage", async: false, 
        success: function( data ) {
            data = JSON.parse(data);
            var gauge_id = "#" + gauge_name + "-usage";
            var preval = parseInt($( gauge_id ).val());
            var newval = data["percentage"];
            animate_gauge($( gauge_id ), preval, newval);
        }
    });
}

//when the document is ready, update the gauges every three seconds.
$(document).ready(function($) {    
    setInterval(function() {
     
        run_gauge("cpu");
        run_gauge("memory");
        run_gauge("disk");
        run_gauge("temperature")
        //leveraging jQuery Knob for gauge UI.
        $(".knob").knob();

    }, 3000);   
});