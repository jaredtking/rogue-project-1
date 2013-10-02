var QuizController = Ember.ObjectController.extend({
	actions: {
		startQuiz: function() {
			console.log('Starting quiz');

			// retrieves the quiz order loaded from API
			App.quiz = this.get('quiz');
			App.q = 1;

			this.transitionToRoute('contentitem', App.q);
		}
	}
});

module.exports = QuizController;