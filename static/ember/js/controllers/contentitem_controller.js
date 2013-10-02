var ContentitemController = Ember.ObjectController.extend({
	actions: {
		markSuspicious: function() {
			console.log('Making a post trust request');
			var url = App.api + '/contentitems/' + this.get('imageId');

			// perform API call
			App.postJSON(App.api + '/trustdecision/', {
				user: null,
				decision: false,
				ctype: this.get('contentType'),
				cid: this.get('imageId')
			});

			App.q++;
			if (App.q > App.quiz.length) {
				console.log('Quiz finished');
				this.transitionToRoute('finish');
			} else {
				console.log('Moving on to next item');
				this.transitionToRoute('contentitem', App.q);
			}
		},
		markTrustworthy: function() {
			console.log('Making a post trust request');
			var url = App.api + '/contentitems/' + this.get('imageId');

			// perform API call
			App.postJSON(App.api + '/trustdecision/', {
				user: null,
				decision: true,
				ctype: this.get('contentType'),
				cid: this.get('imageId')
			});

			App.q++;
			if (App.q > App.quiz.length) {
				console.log('Quiz finished');
				this.transitionToRoute('finish');
			} else {
				console.log('Moving on to next item');
				this.transitionToRoute('contentitem', App.q);
			}
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