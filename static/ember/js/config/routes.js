var App = require('./app');

App.Router.map(function() {
	this.route('contentitem', { path: '/:contentitem_type/:contentitem_id'} );
	this.route('quiz', { path: '/'} );
	this.route('quiz', { path: '/finish'} );
});

