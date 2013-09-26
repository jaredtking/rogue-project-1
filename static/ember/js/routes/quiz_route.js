var QuizRoute = Ember.Route.extend({
	model: function(params){
		var url = '/quiz/generate';
		return App.getJSON(url, params);
	}
});

module.exports = QuizRoute;