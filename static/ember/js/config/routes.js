var App = require('./app');

App.Router.map(function() {
	this.route('contentitem', { path: '/:q'} );
	this.route('start', { path: '/'} );
	this.route('finish', { path: '/finish'} );
});

