var ContentitemController = Ember.ObjectController.extend({
	actions: {
		markSuspicious: function() {
			console.log('Making a put trust request');
			var url = App.api + '/contentitems/'+this.get('id');

			// perform API call
			// TODO

			console.log('Moving on to next item');
			// TODO
		},
		markTrustworthy: function() {
			console.log('Making a put trust request');
			var url = App.api + '/contentitems/'+this.get('id');

			// perform API call
			// TODO

			console.log('Moving on to next item');
			// TODO
		}
	},
	isEmailContentType: function(){
		return this.get('contentType') == "email";
	}.property('contentType'),
	isSocialMediaContentType: function(){
		return this.get('contentType') == "socialmedia";
	}.property('contentType'),
	isWebSiteContentType: function(){
		return this.get('contentType') == "webpage";
	}.property('contentType'),
	imageUrl: function(){
		return "/static/imgs/" + this.get('contentType') + "-" + this.get('imageId') +".png";
	}.property('imageId', 'contentType'),
});

module.exports = ContentitemController;