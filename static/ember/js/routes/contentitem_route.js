var ContentitemRoute = Ember.Route.extend({
	model: function(params){
		params = App.quiz[params.q-1];

		var url = App.api + '/' + params.contentitem_type + '/' + params.contentitem_id;

		return App.getJSON(url, params);
	},
});

module.exports = ContentitemRoute;