var ContentitemRoute = Ember.Route.extend({
	model: function(params){
		var url = App.api + '/' + params.contentitem_type + '/' + params.contentitem_id;
		return App.getJSON(url, params);
	}
});

module.exports = ContentitemRoute;