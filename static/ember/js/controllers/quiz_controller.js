var QuizController = Ember.ObjectController.extend({
	actions: {
		startQuiz: function() {
			console.log('Starting quiz');

			// retrieves the quiz order loaded from API
			var quiz = this.get('quiz');

			// PROBLEM model not loading
			this.transitionToRoute('contentitem', quiz[0]);
		}
	}
});

module.exports = QuizController;