(function(){
	'use strict';

	angular.module('vehiclesmodel').config(config);

	function config($routeProvider) {
      $routeProvider.
        when('/vehiclesmodel', {
			template: '<vehiclesmodel-list></vehiclesmodel-list>',
        });
    }
})();