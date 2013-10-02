// require other, dependencies here, ie:
// require('./vendor/moment');

//require('../vendor/jquery');
//require('../vendor/handlebars.js');
//require('../vendor/ember');
//require('../vendor/bs-for-ember/js/bs-core.max')
require('../vendor/ember-data'); // delete if you don't want ember-data

var App = Ember.Application.createWithMixins(Bootstrap.Register, {
	rootElement: $('#application')
});
App.Store = require('./store'); // delete if you don't want ember-data

//Define any global variables or functions here using the 'App' namespace
App.api = "/api"
App.debug = true;

function getCookie(name) {
     var cookieValue = null;
     if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
             var cookie = jQuery.trim(cookies[i]);
             // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) == (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
         }
     }
 }
 return cookieValue;
}

//Makes a promise-based POST request to the 'url' with the given 'data'
App.postJSON = function(url, data){
	var token = getCookie('csrftoken');
	Ember.$.ajax({
	    url: url,
	    headers: {"X-CSRFToken": token},
	    type: "POST",
	    dataType: "json",
	    contentType:"application/json",
	    data: JSON.stringify(data)
	})
	.then(function(){if(App.debug){console.log('POST Request to ' +url+' was successful.')}})
	.fail(function(){if(App.debug){console.log('POST Request to' +url+' with data: '+JSON.stringify(data)+' failed.')}})
}

//Makes a promise-based PUT request to the 'url' with the given 'data'
App.putJSON = function(url, data){
	var token = $('meta[name="csrf-token"]').attr('content');
	Ember.$.ajax({
	    url: url,
	    headers: {"X-CSRFToken": token},
	    type: "PUT",
	    dataType: "json",
	    contentType:"application/json",
	    data: JSON.stringify(data)
	})
	.then(function(){if(App.debug){console.log('PUT Request to ' +url+' was successful.')}})
	.fail(function(){if(App.debug){console.log('PUT Request to' +url+' with data: '+JSON.stringify(data)+' failed.')}})
}

//Makes a promise-based GET request to the 'url'
App.getJSON = function(url, params){
	return Ember.$.getJSON(url)
		.then(function(data) {
      		if(App.debug){console.log('GET Request to ' +url+' was successful.');}
      		data.contentType = params.contentitem_type;
			return data;
    	})
    	.fail(function(request, status, error){
    		if(App.debug){console.log('GET Request to' +url+' failed with the response: '+request.responseText)}
    	});
}

//Finds cookieName in window.document.cookie
App.getCookie = function (cookieName){
	
	var cookieValue = document.cookie;
	var start = cookieValue.indexOf(" " + cookieName + "=");
	if (start == -1){
		start = cookieValue.indexOf(cookieName + "=");
	}
	if (start == -1){
	  	cookieValue = null;
	}
	else {
	  	start = cookieValue.indexOf("=", start) + 1;
	  	var end = cookieValue.indexOf(";", start);
	  	if (end == -1){
	    	end = cookieValue.length;
	    }
	  	cookieValue = unescape(cookieValue.substring(start,end));
	}
	return cookieValue;
};

//Adds cookieName in window.document.cookie following the 
//format cookieName=value, where exdays sets the expiration date. exdays=null implies session cookie.
App.setCookie = function (cookieName,value,exdays){
	var exdate = new Date();
	exdate.setDate(exdate.getDate() + exdays);
	var cookieValue = escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
	document.cookie = cookieName + "=" + cookieValue;
};

module.exports = App;

