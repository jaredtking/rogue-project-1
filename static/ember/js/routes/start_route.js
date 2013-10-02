var QuizRoute = Ember.Route.extend({
	model: function(params){
		var url = '/quiz/generate';
		return App.getJSON(url, params);
	},
	actions: {
    	moveTo: function(context){
    		var quiz = this.get('quiz');
        	this.transitionTo('contentitem', quiz[0]);
    	}
	}
});

module.exports = QuizRoute;