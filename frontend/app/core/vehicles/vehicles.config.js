(function(){
	'use strict';

	angular.module('vehicles').config(config);

	function config($routeProvider) {
      $routeProvider.
        when('/vehicles', {
			template: '<vehicles-list></vehicles-list>',
        });
    }

})();

