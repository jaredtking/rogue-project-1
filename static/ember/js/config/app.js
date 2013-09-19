// require other, dependencies here, ie:
// require('./vendor/moment');

//require('../vendor/jquery');
//require('../vendor/handlebars.js');
//require('../vendor/ember');
//require('../vendor/bs-for-ember/js/bs-core.max')
require('../vendor/ember-data'); // delete if you don't want ember-data

var App = Ember.Application.createWithMixins(Bootstrap.Register);
App.Store = require('./store'); // delete if you don't want ember-data

module.exports = App;